import requests, json
from etl.extract_tranform.src.build_tables import contacts

contacts_table = contacts.complete_table()

url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/contact'
response = requests.put(url, json.dumps(contacts_table))