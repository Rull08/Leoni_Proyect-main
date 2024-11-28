import pg8000
import os 
from dotenv import load_dotenv

load_dotenv()

db_connect = {
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def get_connection():
    return pg8000.connect(**db_connect)