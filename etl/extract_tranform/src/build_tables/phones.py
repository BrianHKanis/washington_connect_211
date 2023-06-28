import hashlib
from ..airtable_client import build_dict, single_string_value_from_list, add_dpmgid
from ...data.hsds_columns import phones_columns

required= ['id', 'number']

def rename_columns(core_dict: list) -> list:
    for record in core_dict:
        if 'location_ids' in record.keys():
            record['location_id'] = record['location_ids']
        if 'service_ids' in record.keys():
            record['service_id'] = record['service_ids']
        if 'organization_ids' in record.keys():
            record['organization_id'] = record['organization_ids']
        if 'contacts' in record.keys():
            record['contact_id'] = record['contacts']
        if 'interpretation' in record.keys():
            record['language'] = record['interpretation']
    return core_dict

def delete_columns(core_dict):
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in phones_columns:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict):
    for record in core_dict:
        for required_key in required:
            if required_key not in record.keys():
                record[required_key] = ' '
    return core_dict

def build_record(record, id_to_hash, key):
    new_record = record.copy()
    #new_record['source_id'] = record['id']
    new_record[key] = [id_to_hash]
    new_record['id'] = hashlib.md5(((record['id'] + id_to_hash)).encode('utf-8')).hexdigest()
    return new_record


def duplicate_for_locations(core_dict):
    for record in core_dict:
        if 'location_id' in record.keys(): 
            if len(record['location_id']) > 1:
                org_ids = record['location_id']
                for org_id in org_ids:
                    new_record = build_record(record, org_id, 'location_id')
                    core_dict.append(new_record)
                core_dict.remove(record)
    return core_dict

def duplicate_for_services(core_dict):
    for record in core_dict:
        if 'service_id' in record.keys(): 
            if len(record['service_id']) > 1:
                org_ids = record['service_id']
                for org_id in org_ids:
                    new_record = build_record(record, org_id, 'service_id')
                    core_dict.append(new_record)
                core_dict.remove(record)
    return core_dict

def duplicate_for_organizations(core_dict):
    for record in core_dict:
        if 'organization_id' in record.keys(): 
            if len(record['organization_id']) > 1:
                org_ids = record['organization_id']
                for org_id in org_ids:
                    new_record = build_record(record, org_id, 'organization_id')
                    core_dict.append(new_record)
                core_dict.remove(record)
    return core_dict

def duplicate_all(core_dict):
    duplicate_for_locations(core_dict)
    duplicate_for_services(core_dict)
    duplicate_for_organizations(core_dict)
    return core_dict

def complete_table():
    phone_records = build_dict('phones')
    phone_hsds = rename_columns(phone_records)
    phones_with_deletes = delete_columns(phone_hsds)
    phones = add_required_if_missing(phones_with_deletes)
    phones_with_duplicates = duplicate_all(phones)
    phones_with_strings = single_string_value_from_list(phones_with_duplicates, ['location_id', 'service_id', 'organization_id'])
    phones_with_dpmgid = add_dpmgid(phones_with_strings)
    return phones_with_dpmgid
