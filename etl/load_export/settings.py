from dotenv import load_dotenv
import os

load_dotenv()

api_writer_root_url = os.getenv('API_WRITER_ROOT_URL')
api_reader_root_url = os.getenv('API_READER_ROOT_URL')

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

LOCAL_DB_NAME = os.getenv('LOCAL_DB_NAME')
LOCAL_DB_USER = os.getenv('LOCAL_DB_USER')
LOCAL_DB_PASSWORD = os.getenv('LOCAL_DB_PASSWORD')