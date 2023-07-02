from ..airtable_client import build_dict, single_string_value_from_list, rename_columns, delete_columns, add_required_if_missing, string_to_integer, duplicate_record_if_multiple_foreign_keys

required_keys = ['id', 'number']
phone_columns = ['id', 'location_id', 'service_id', 'organization_id', 'contact_id', 'service_at_location_id', 'number', 'extension', 'type', 'description', 'languages', 'attributes', 'metadata']
columns_to_rename = {'location_ids': 'location_id', 'service_ids': 'service_id',
                     'organization_ids': 'organization_id', 'contacts': 'contact_id'}
foreign_keys_to_duplicate = ['location_id', 'service_id', 'organization_id']
columns_with_lists = ['location_id', 'service_id', 'organization_id', 'contact_id']

def complete_table():
    phone_records = build_dict('phones')
    phone_hsds = rename_columns(phone_records, columns_to_rename)
    phones_with_deletes = delete_columns(phone_hsds, phone_columns)
    phones = add_required_if_missing(phones_with_deletes, required_keys)
    phones_with_duplicates = duplicate_record_if_multiple_foreign_keys(phones, foreign_keys_to_duplicate)
    duplicate_record_if_multiple_foreign_keys(phones_with_duplicates, foreign_keys_to_duplicate)
    duplicate_record_if_multiple_foreign_keys(phones_with_duplicates, foreign_keys_to_duplicate)
    # Ran 3 times
    phones_with_strings = single_string_value_from_list(phones_with_duplicates, columns_with_lists)
    phones_with_correct_data_types = string_to_integer(phones_with_strings, 'extension')
    return phones_with_correct_data_types
