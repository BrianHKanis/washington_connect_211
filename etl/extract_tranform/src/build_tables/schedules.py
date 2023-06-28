import hashlib
from ..airtable_client import build_dict, single_string_value_from_list, add_dpmgid
from ...data.hsds_columns import schedule_columns

required = ['id']

def rename_columns(core_dict):
    for record in core_dict:
        if 'location_ids' in record.keys():
            record['location_id'] = record['location_ids']
        if 'service_ids' in record.keys():
            record['service_id'] = record['service_ids']
        
    return core_dict

def delete_columns(core_dict):    
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in schedule_columns:
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

def duplicate_all(core_dict):
    duplicate_for_locations(core_dict)
    duplicate_for_services(core_dict)
    return core_dict

#Testing
def remove_column(core_dict, column_name):
    for record in core_dict:
        if column_name in record.keys(): 
            del record[column_name]
    return core_dict

def complete_table():
    schedule_records = build_dict('schedules')
    schedule_hsds = rename_columns(schedule_records)
    schedule_with_deletes = delete_columns(schedule_hsds)
    schedules = add_required_if_missing(schedule_with_deletes)
    schedules_with_duplicates = duplicate_all(schedules)
    duplicate_all(schedules_with_duplicates) # Twice for 2 records
    schedules_with_strings = single_string_value_from_list(schedules_with_duplicates, ['location_id', 'service_id'])
    schedules_with_dpmgid = add_dpmgid(schedules_with_strings)
    remove_column(schedules_with_dpmgid, 'byday')
    remove_column(schedules_with_dpmgid, 'interval')
    return schedules_with_dpmgid