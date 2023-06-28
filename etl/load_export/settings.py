from dotenv import load_dotenv
import os

load_dotenv()
api_writer_root_url = os.getenv('API_WRITER_ROOT_URL')
api_reader_root_url = os.getenv('API_READER_ROOT_URL')