import time
import json
import random
from confluent_kafka import Producer
from datetime import datetime
from const import KAFKA_BOOTSTRAP_SERVERS, TOPIC_RAW_TEMPERATURE

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def main():
    conf = {
        'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    }

    producer = Producer(conf)
    topic = TOPIC_RAW_TEMPERATURE

    print("Sensor started. Producing temperature readings...")

    try:
        while True:
            temperature = round(random.uniform(20.0, 30.0), 2)
            timestamp = datetime.now().isoformat()
            
            data = {
                'value': temperature,
                'timestamp': timestamp
            }
            
            producer.produce(
                topic, 
                key=str(timestamp), 
                value=json.dumps(data), 
                callback=delivery_report
            )
            
            producer.flush()
            
            print(f"Sent: {data}")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("Sensor stopped.")

if __name__ == '__main__':
    main()
