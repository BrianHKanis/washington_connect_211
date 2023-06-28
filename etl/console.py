from load_export.src.api_export import *
from load_export.settings import api_writer_root_url
import requests
from dotenv import load_dotenv

load_dotenv()
merged = merge_endpoints()
# export_files(api_writer_root_url, merged)
# org_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/organization'
# org_upload = requests.put(org_url, json.dumps(merged['organization']))
# org_response = requests.get(org_url)
# Fix -> Done
# loc_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/location'
# loc_upload = requests.put(loc_url, json.dumps(merged['location']))
# loc_response = requests.get(loc_url)
# Fix -> Done
# srv_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/service'
# srv_upload = requests.put(srv_url, json.dumps(merged['service']))
# srv_response = requests.get(srv_url)
# sal_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/service_at_location'
# sal_upload = requests.put(sal_url, json.dumps(merged['service_at_location']))
# sal_response = requests.get(sal_url)
# contact_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/contact'
# contact_upload = requests.put(contact_url, json.dumps(merged['contact']))
# contact_response = requests.get(contact_url)

test_rec = [{'dpmgid': '69', 'id': 'rec02nHqo1dX4YdzF', 'name': 'Sun House', 'organization_id': ' '}]

def get_all_keys(table_name):
    keys = []
    records = merged[table_name]
    for record in records:
        for key in record.keys():
            if key not in keys:
                keys.append(key)
    return keys

def return_all_fields_of_column(table_name, column_name):
    records = merged[table_name]
    for record in records:
        if column_name in record.keys():
            print(record[column_name])

def return_records_with_list(table_name):
    records = merged[table_name]
    for record in records:
        keys = record.keys()
        for key in keys:
            if type(record[key]) == list:
                print(record[key])
    

# Fix
sch_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/schedule'
sch_upload = requests.put(sch_url, json.dumps(merged['schedule']))
sch_response = requests.get(sch_url)


# # Fix
phone_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/phone'
phone_upload = requests.put(phone_url, json.dumps(merged['phone']))
phone_response = requests.get(phone_url)

# taxonomy_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/taxonomy'
# taxonomy_upload = requests.put(taxonomy_url, json.dumps(merged['taxonomy']))
# taxonomy_response = requests.get(taxonomy_url)

# taxonomy_term_url = 'https://lobster-app-yqmp3.ondigitalocean.app/whatcom-writer/hsds3/taxonomy_term'
# taxonomy_term_upload = requests.put(taxonomy_term_url, json.dumps(merged['taxonomy_term']))
# taxonomy_term_response = requests.get(taxonomy_term_url)

# reader = 'https://lobster-app-yqmp3.ondigitalocean.app/wardc-reader/hsds3/'