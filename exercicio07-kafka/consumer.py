from kafka import KafkaConsumer, KafkaProducer
from const import *
import sys

consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])
producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

try:
  topic = sys.argv[1]
except:
  print ('Usage: python3 consumer <topic_name>')
  exit(1)
  
consumer.subscribe([topic])
for msg in consumer:
    msgStr = str(msg.value)
    print(msgStr)
    producer.send(topic + '_reply', value=msgStr.encode())
    producer.flush()
