import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
TOPIC_RAW_TEMPERATURE = 'raw_temperature'
TOPIC_PROCESSED_TEMPERATURE = 'processed_temperature'

# REST API
REST_SERVER_ADDRESS = os.getenv('REST_SERVER_ADDRESS', 'localhost:8000')
REST_SERVER_URL = f"http://{REST_SERVER_ADDRESS}"

# Processor
WINDOW_SIZE = 5

# Database
DB_PATH = 'temperature.db'
