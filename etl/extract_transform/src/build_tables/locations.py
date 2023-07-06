from ..airtable_client import build_dict, single_string_value_from_list, rename_columns, delete_columns, add_required_if_missing, build_duplicate_record, duplicate_record_if_multiple_foreign_keys

required_keys = ['id', 'location_type', 'organization_id']
locations_columns = ["id", "location_type", "url", "organization_id", "name",
                "alternate_name", "description", "transportation", "latitude",
                "longitude", "external_identifier", "external_identifier_type",
                "languages", "addresses", "contacts", "accessibility", "phones",
                "schedules", "attributes", "metadata"]

columns_to_rename = {'schedule': 'schedules', 'organization_ids': 'organization_id'}

foreign_keys_to_duplicate = ['organization_id']
columns_with_lists_to_convert = ['organization_id']

def complete_table():
    location_records = build_dict('locations')
    locations_hsds = rename_columns(location_records, columns_to_rename)
    locations_with_deletes = delete_columns(locations_hsds, locations_columns)
    locations = add_required_if_missing(locations_with_deletes, required_keys)
    locations_with_dups = duplicate_record_if_multiple_foreign_keys(locations, foreign_keys_to_duplicate)
    locations_with_strings = single_string_value_from_list(locations_with_dups, columns_with_lists_to_convert)
    return locations_with_strings