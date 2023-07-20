import requests, json
import hashlib
from ..settings import airtable_key, base_id

headers = {'Authorization': f'Bearer {airtable_key}'}
table_id_dict = {'organizations': 'tblqoitqeXyTPwU8i', 'services': 'tbl55axdd1ToQnD8a',
                 'locations': 'tblupy32maGd0av6I', 'phones': 'tblvSTMIx5OJBnV2m',
                 'x-verification': 'tblhWvHJVmlgpIdVc', 'taxonomy_terms': 'tblGdXYo1onpkh7ow',
                 'schedules': 'tblDtGJOo2adZBWui', 'x-taxonomies': 'tbljWxEZPvYL3CmVU',
                 'physical_addresses': 'tblo9O05Tcxuhm5ro', 'contacts': 'tblX4DJEnxDCd3d6e'}

def make_request(table_name):
    url = f'https://api.airtable.com/v0/{base_id}/'
    request_url = url + table_id_dict[table_name]
    response = requests.get(request_url, headers=headers)
    if response.status_code != 200:
        raise Exception("Unable to Connect Air Table. Please check your authentication keys") 
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

def rename_columns(core_dict, columns_to_rename_dict):
    for record in core_dict:
            for k, v in columns_to_rename_dict.items():
                if k in record.keys():
                    new_key = v
                    values = record[k]
                    record[new_key] = values
    return core_dict
    
def delete_columns(core_dict, columns_list):    
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in columns_list:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict, required_keys):
    for record in core_dict:
        record['dpmgid'] = '69'
        for required_key in required_keys:
            if required_key not in record.keys():
                record[required_key] = ""
    return core_dict

def build_duplicate_record(record, id_to_hash, key):
    new_record = record.copy()
    new_record['source_id'] = record['id']       #Talk to Skyler to add to schema
    new_record[key] = [id_to_hash]
    new_record['id'] = hashlib.md5(((record['id'] + id_to_hash)).encode('utf-8')).hexdigest()
    return new_record

def duplicate_record_if_multiple_foreign_keys(core_dict, column_names):
    records_to_remove = []
    for record in core_dict:
        for column_name in column_names:
            if column_name in record.keys():
                if type(record[column_name]) == list and len(record[column_name]) > 1: 
                    foreign_keys = record[column_name]
                    new_records = [build_duplicate_record(record, foreign_key, column_name) for foreign_key in foreign_keys]
                    [core_dict.append(record) for record in new_records]
                    records_to_remove.append(record)
    for record in records_to_remove:
        core_dict.remove(record)
    return core_dict

def list_to_string(core_dict, column_name):
    for record in core_dict:
        if column_name in record.keys():
            column_string = ', '.join(record[column_name])
            record[column_name] = column_string
    return core_dict

def string_to_integer(core_dict, column_name):
    for record in core_dict:
        if column_name in record.keys():
            column_int = int(record[column_name])
            record[column_name] = column_int
    return core_dict

def remove_columns(core_dict, column_names):
    for record in core_dict:
        for column_name in column_names:
            if column_name in record.keys(): 
                del record[column_name]
    return core_dict