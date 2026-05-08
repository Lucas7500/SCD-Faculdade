import json
import sqlite3
import threading
import grpc
from concurrent import futures
from confluent_kafka import Consumer, KafkaError
from const import KAFKA_BOOTSTRAP_SERVERS, TOPIC_PROCESSED_TEMPERATURE, GRPC_SERVER_ADDRESS, DB_PATH
import temperature_pb2
import temperature_pb2_grpc


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL,
            timestamp TEXT,
            type TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(value, timestamp, data_type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO measurements (value, timestamp, type)
        VALUES (?, ?, ?)
    ''', (value, timestamp, data_type))
    conn.commit()
    conn.close()

class TemperatureServiceServicer(temperature_pb2_grpc.TemperatureServiceServicer):
    def GetLatestTemperature(self, request, context):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT value, timestamp, type FROM measurements ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        conn.close()

        if row:
            return temperature_pb2.TemperatureData(value=row[0], timestamp=row[1], type=row[2])
        return temperature_pb2.TemperatureData(value=0.0, timestamp="N/A", type="none")

    def GetHistoricalData(self, request, context):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT value, timestamp, type FROM measurements ORDER BY id DESC LIMIT 10')
        rows = cursor.fetchall()
        conn.close()

        readings = [temperature_pb2.TemperatureData(value=r[0], timestamp=r[1], type=r[2]) for r in rows]
        return temperature_pb2.TemperatureHistory(readings=readings)

def kafka_consumer_thread():
    consumer_conf = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'web-service-gorup',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    consumer.subscribe([TOPIC_PROCESSED_TEMPERATURE])

    print("Kafka Consumer started...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None: 
                continue
            elif msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF: 
                    continue
                else:
                    print(msg.error())
                    break
            
            data = json.loads(msg.value().decode('utf-8'))
            print(f"Saving to DB: {data}")
            save_to_db(data['value'], data['timestamp'], data['type'])
    except Exception as e:
        print(f"Consumer error: {e}")
    finally:
        consumer.close()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    temperature_pb2_grpc.add_TemperatureServiceServicer_to_server(TemperatureServiceServicer(), server)
    server.add_insecure_port(GRPC_SERVER_ADDRESS)
    print(f"gRPC Server started on {GRPC_SERVER_ADDRESS}...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    init_db()
    threading.Thread(target=kafka_consumer_thread, daemon=True).start()
    serve()
