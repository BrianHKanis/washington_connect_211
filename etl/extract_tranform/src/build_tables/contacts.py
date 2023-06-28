import hashlib
from ..airtable_client import build_dict, single_string_value_from_list, add_dpmgid
from ...data.hsds_columns import contact_columns

required = ['id']

def rename_columns(core_dict):
    for record in core_dict:
        if 'services' in record.keys():
            record['service_id'] = record['services']
    return core_dict

def delete_columns(core_dict):    
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in contact_columns:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict):
    for record in core_dict:
        for required_key in required:
            if required_key not in record.keys():
                record[required_key] = " "
    return core_dict

def build_record(record, id_to_hash, key):
    new_record = record.copy()
    new_record['source_id'] = record['id']
    new_record[key] = [id_to_hash]
    new_record['id'] = hashlib.md5(((record['id'] + id_to_hash)).encode('utf-8')).hexdigest()
    return new_record

def duplicate_for_services(core_dict):
    for record in core_dict:
        if 'service_id' in record.keys():
            if type(record['service_id']) == list: 
                if len(record['service_id']) > 1:
                    service_ids = record['service_id']
                    for service_id in service_ids:
                        new_record = build_record(record, service_id, 'service_id')
                        core_dict.append(new_record)
                    core_dict.remove(record)
    return core_dict

def complete_table():
    contact_records = build_dict('contacts')
    contact_hsds = rename_columns(contact_records)
    contact_with_deletes = delete_columns(contact_hsds)
    contacts = add_required_if_missing(contact_with_deletes)
    contacts_with_duplicates = duplicate_for_services(contacts)
    duplicate_for_services(contacts_with_duplicates)
    contacts_with_strings = single_string_value_from_list(contacts_with_duplicates, ['service_id'])
    contacts_with_dpmgid = add_dpmgid(contacts_with_strings)
    return contacts_with_dpmgid