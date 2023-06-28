import requests, os, json
from extract_tranform.src.load_all import load_all_tables

topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']

def merge_endpoints():
    files = load_all_tables()
    endpoints = topic_names
    merged = dict(zip(endpoints, files))
    return merged

def export_files(root_url, merged):
    for k, v in merged.items():
        url = root_url + str('/hsds3/') + str(k)
        status = requests.put(url, json.dumps(v))
        return status.json()

