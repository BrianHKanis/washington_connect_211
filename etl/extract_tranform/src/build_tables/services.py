from ..airtable_client import build_dict, single_string_value_from_list, rename_columns, delete_columns, add_required_if_missing, duplicate_record_if_multiple_foreign_keys, list_to_string

required_keys = ['id', 'name', 'status', 'organization_id']
service_columns = ["id", "organization_id", "program_id", "name", "alternate_name",
            "description", "url", "email", "status", "interpretation_services",
            "application_process", "fees_description", "wait_time", "fees",
            "accreditations", "eligibility_description", "minimum_age", "maximum_age",
            "assured_date", "assurer_email", "licenses", "alert", "last_modified",
            "service_areas", "service_at_locations", "languages",
            "organization", "funding", "cost_options", "program", "required_documents",
            "attributes", "metadata"]
columns_to_rename = {'schedule': 'schedules', 'organization_ids': 'organization_id'}
foreign_keys_to_duplicate = ['organization_id']

def change_data_type(core_dict):
    for record in core_dict:
        if 'interpretation_services' in record.keys(): 
            inter_services = ', '.join(record['interpretation_services'])
            record['interpretation_services'] = inter_services

def complete_table():
    service_records = build_dict('services')
    services_hsds = rename_columns(service_records, columns_to_rename)
    services_with_deletes = delete_columns(services_hsds, service_columns)
    services = add_required_if_missing(services_with_deletes, required_keys)
    services_with_duplicates = duplicate_record_if_multiple_foreign_keys(services, foreign_keys_to_duplicate)
    services_with_strings = single_string_value_from_list(services_with_duplicates, foreign_keys_to_duplicate)
    services_with_correct_data_types = list_to_string(services_with_strings, 'interpretation_services')
    return services_with_correct_data_types