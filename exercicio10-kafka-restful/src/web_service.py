import json
import sqlite3
import threading
import uvicorn
from fastapi import FastAPI
from confluent_kafka import Consumer, KafkaError
from const import KAFKA_BOOTSTRAP_SERVERS, TOPIC_PROCESSED_TEMPERATURE, REST_SERVER_ADDRESS, DB_PATH

app = FastAPI()

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

@app.get("/latest")
def get_latest_temperature():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT value, timestamp, type FROM measurements ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"value": row[0], "timestamp": row[1], "type": row[2]}
    
    return {"value": 0.0, "timestamp": "N/A", "type": "none"}

@app.get("/history")
def get_historical_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT value, timestamp, type FROM measurements ORDER BY id DESC LIMIT 10')
    rows = cursor.fetchall()
    conn.close()

    readings = [{"value": r[0], "timestamp": r[1], "type": r[2]} for r in rows]
    return {"readings": readings}

def kafka_consumer_thread():
    consumer_conf = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'web-service-group',
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

if __name__ == '__main__':
    init_db()
    threading.Thread(target=kafka_consumer_thread, daemon=True).start()
    
    host, port = REST_SERVER_ADDRESS.split(':')
    uvicorn.run(app, host=host, port=int(port))
