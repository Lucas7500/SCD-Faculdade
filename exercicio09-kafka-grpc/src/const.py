import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
TOPIC_RAW_TEMPERATURE = 'raw_temperature'
TOPIC_PROCESSED_TEMPERATURE = 'processed_temperature'

# gRPC
GRPC_SERVER_ADDRESS = os.getenv('GRPC_SERVER_ADDRESS', 'localhost:50051')

# Processor
WINDOW_SIZE = 5

# Database
DB_PATH = 'temperature.db'
