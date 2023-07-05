from ..airtable_client import build_dict, single_string_value_from_list, rename_columns, delete_columns, add_required_if_missing, duplicate_record_if_multiple_foreign_keys

required_keys = ['id']
contact_columns = ['id', 'organization_id','service_id','service_at_location_id', 'location_id', 'name',
                    'title', 'department', 'email','attributes','metadata']
columns_to_rename_dict = {'services': 'service_id'}
foreign_keys_to_duplicate = ['service_id']

def complete_table():
    contact_records = build_dict('contacts')
    contact_hsds = rename_columns(contact_records, columns_to_rename_dict)
    contact_with_deletes = delete_columns(contact_hsds, contact_columns)
    contacts = add_required_if_missing(contact_with_deletes, required_keys)
    contacts_with_duplicates = duplicate_record_if_multiple_foreign_keys(contacts, foreign_keys_to_duplicate)
   # duplicate_record_if_multiple_foreign_keys(contacts_with_duplicates, foreign_keys_to_duplicate)
    # Ran twice
    contacts_with_strings = single_string_value_from_list(contacts_with_duplicates, foreign_keys_to_duplicate)
    return contacts_with_strings