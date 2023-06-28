import hashlib
from ..airtable_client import build_dict, single_string_value_from_list, add_dpmgid
from ...data.hsds_columns import services_columns

required = ['id', 'name', 'status', 'organization_id']

def rename_columns(core_dict):
    for record in core_dict:
        if 'schedule' in record.keys():
            record['schedules'] = record['schedule']
        if 'organization_ids' in record.keys():
            record['organization_id'] = record['organization_ids']
    return core_dict

def delete_columns(core_dict):
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in services_columns:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict):
    for record in core_dict:
        for required_key in required:
            if required_key not in record.keys():
                record[required_key] = ' '
    return core_dict

def build_record(record, id_to_hash):
    new_record = record.copy()
    # new_record['source_id'] = record['id']
    new_record['organization_id'] = [id_to_hash]
    new_record['id'] = hashlib.md5(((record['id'] + id_to_hash)).encode('utf-8')).hexdigest()
    return new_record

def duplicate_if_array_not_required(core_dict):
    for record in core_dict:
        if 'organization_id' in record.keys(): 
            if len(record['organization_id']) > 1:
                org_ids = record['organization_id']
                for org_id in org_ids:
                    new_record = build_record(record, org_id)
                    core_dict.append(new_record)
                core_dict.remove(record)
    return core_dict

#Testing
def remove_column(core_dict, column_name):
    for record in core_dict:
        if column_name in record.keys(): 
            del record[column_name]
    return core_dict

def complete_table():
    service_records = build_dict('services')
    services_hsds = rename_columns(service_records)
    services_with_deletes = delete_columns(services_hsds)
    services = add_required_if_missing(services_with_deletes)
    services_with_duplicates = duplicate_if_array_not_required(services)
    duplicate_if_array_not_required(services)
    services_with_strings = single_string_value_from_list(services_with_duplicates, ['organization_id'])
    single_string_value_from_list(services_with_duplicates, ['organization_id'])
    services_with_dpmgid = add_dpmgid(services_with_strings)
    remove_column(services_with_dpmgid, 'interpretation_services') #Schema should allow list
    return services_with_dpmgid