from dotenv import load_dotenv
import os

load_dotenv()
airtable_key = os.getenv('AIRTABLE_KEY')
base_id = os.getenv('BASE_ID')

