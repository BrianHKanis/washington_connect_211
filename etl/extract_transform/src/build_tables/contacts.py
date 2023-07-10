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
    breakpoint()
    contacts_with_duplicates = duplicate_record_if_multiple_foreign_keys(contacts, foreign_keys_to_duplicate)
    breakpoint()
    #duplicate_record_if_multiple_foreign_keys(contacts_with_duplicates, foreign_keys_to_duplicate)
    # Ran twice
    contacts_with_strings = single_string_value_from_list(contacts_with_duplicates, foreign_keys_to_duplicate)
    return contacts_with_strings

# Not Duplicated first time
#{'name': 'Mount Baker School District Family Services Coordinators', 'id': 'recCXNf1liimWnh5S', 'service_id': ['recd6UHNm7OTtwMqC', 'recCv40TC9857KCPE'], 'dpmgid': '69'}
#{'name': 'Compass Health Local Access Department Line', 'id': 'receYJz9nV1DSRYVW', 'service_id': ['rec6JAvIRZ78HD6wH', 'recbSyuJIZPXXj3LG'], 'dpmgid': '69'}

# Is Duplicated first time
#{'name': 'Compass Health Local Access Department Line', 'id': 'receYJz9nV1DSRYVW', 'service_id': ['rec6JAvIRZ78HD6wH', 'recbSyuJIZPXXj3LG'], 'dpmgid': '69'}
#{'name': 'Compass Health Administration and General Information Line', 'id': 'recd7jy7KN1QCPLFc', 'service_id': ['recoks2DPAZqnzamd', 'rec6JAvIRZ78HD6wH', 'recbSyuJIZPXXj3LG'], 'dpmgid': '69'}