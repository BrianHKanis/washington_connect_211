import requests, os, json
from ...extract_transform.src.load_all import load_all_tables

topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']

def merge_endpoints():
    files = load_all_tables()
    endpoints = topic_names
    merged = dict(zip(endpoints, files))
    return merged

def export_files(root_url):
    merged = merge_endpoints()
    for k, v in merged.items():
        url = root_url + str('/hsds3/') + str(k)
        status = requests.put(url, json.dumps(v))
        # try:
        #     if status.status_code == 204:
        #         print(f'{url} end point not reachable throwing status code {status.status_code}')
        #     if status.status_code == 404:
        #         print(f'{url}  Failed with {status.status_code}')
        # except requests.exceptions.ConnectionError:        
        #     continue
    return print('Done')

