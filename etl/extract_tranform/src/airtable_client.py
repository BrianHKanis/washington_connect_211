import requests
from ..data.hsds_columns import table_id_dict
from ..settings import airtable_key, base_id

headers = {'Authorization': f'Bearer {airtable_key}'}

def make_request(table_name):
    url = f'https://api.airtable.com/v0/{base_id}/'
    request_url = url + table_id_dict[table_name]
    response = requests.get(request_url, headers=headers)
    return response

def get_next_url(url, records_json):
    if 'offset' in records_json.keys():
        offset = records_json['offset']
        offset_url = f'/?offset={offset}'
        next_url = url + offset_url
        return next_url
    
def add_pages(url, next_url, records_list):
    while True:
        next_json = requests.get(next_url, headers=headers).json()
        next_records_list = next_json['records']
        records_list.extend(next_records_list)
        if 'offset' in next_json.keys():
            next_url = url + f"/?offset={next_json['offset']}"
        else:
            break

def build_dict(table_name):
    url = f'https://api.airtable.com/v0/{base_id}/{table_id_dict[table_name]}'
    records_json = make_request(table_name).json()
    records_list = records_json['records']
    if 'offset' in records_json.keys():
        next_url = get_next_url(url, records_json)
        add_pages(url, next_url, records_list)
    return [record['fields'] for record in records_list]

def single_string_value_from_list(table, key_names):
    for record in table:
        for key_name in key_names:
            if key_name in record.keys():
                if len(record[key_name]) == 1:
                    record[key_name] = record[key_name][0]
    return table

def add_dpmgid(table):
    for record in table:
        record['dpmgid'] = '69'
    return table