import json
from confluent_kafka import Consumer, Producer, KafkaError
from datetime import datetime
from const import KAFKA_BOOTSTRAP_SERVERS, TOPIC_RAW_TEMPERATURE, TOPIC_PROCESSED_TEMPERATURE, WINDOW_SIZE

def main():
    consumer_conf = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'processor-group',
        'auto.offset.reset': 'earliest'
    }

    producer_conf = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS
    }

    consumer = Consumer(consumer_conf)
    producer = Producer(producer_conf)

    consumer.subscribe([TOPIC_RAW_TEMPERATURE])

    readings = []

    print("Processor started. Waiting for messages...")

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            data = json.loads(msg.value().decode('utf-8'))
            readings.append(data['value'])

            if len(readings) > WINDOW_SIZE:
                readings.pop(0)

            if len(readings) > 0:
                avg_temp = round(sum(readings) / len(readings), 2)
                processed_data = {
                    'value': avg_temp,
                    'timestamp': datetime.now().isoformat(),
                    'type': 'average'
                }

                producer.produce(
                    TOPIC_PROCESSED_TEMPERATURE,
                    key=str(processed_data['timestamp']),
                    value=json.dumps(processed_data)
                )
                producer.flush()
                print(f"Processed: Average Temp = {avg_temp}")

    except KeyboardInterrupt:
        print("Processor stopped.")
    finally:
        consumer.close()

if __name__ == '__main__':
    main()
