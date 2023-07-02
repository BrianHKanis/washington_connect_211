from ..airtable_client import build_dict, single_string_value_from_list, rename_columns, delete_columns, add_required_if_missing, duplicate_record_if_multiple_foreign_keys, remove_columns, list_to_string

required_keys = ['id']
schedule_columns = ['id', 'service_id','location_id','service_at_location_id','valid_from', 'valid_to', 'dtstart',
                     'timezone', 'until',
                'count', 'wkst', 'freq', 'interval', 'byday', 'byweekno', 'bymonthday',
                'byyearday', 'description', 'opens_at', 'closes_at', 'schedule_link',
                'attending_type' ,'notes','attributes','metadata']
columns_to_rename = {'location_ids': 'location_id', 'service_ids': 'service_id'}
foreign_keys_to_duplicate = ['location_id', 'service_id']
columns_to_remove = ['interval', 'bymonthday']

def complete_table():
    schedule_records = build_dict('schedules')
    schedule_hsds = rename_columns(schedule_records, columns_to_rename)
    schedule_with_deletes = delete_columns(schedule_hsds, schedule_columns)
    schedules = add_required_if_missing(schedule_with_deletes, required_keys)
    schedules_with_duplicates = duplicate_record_if_multiple_foreign_keys(schedules, foreign_keys_to_duplicate) 
    duplicate_record_if_multiple_foreign_keys(schedules_with_duplicates, foreign_keys_to_duplicate) 
    # Ran twice 
    schedules_with_strings = single_string_value_from_list(schedules_with_duplicates, foreign_keys_to_duplicate)
    remove_columns(schedules_with_strings, columns_to_remove)
    list_to_string(schedules_with_strings, 'byday')
    return schedules_with_strings