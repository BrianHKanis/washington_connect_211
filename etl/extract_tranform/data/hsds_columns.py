table_id_dict = {'organizations': 'tblqoitqeXyTPwU8i', 'services': 'tbl55axdd1ToQnD8a',
                 'locations': 'tblupy32maGd0av6I', 'phones': 'tblvSTMIx5OJBnV2m',
                 'x-verification': 'tblhWvHJVmlgpIdVc', 'taxonomy_terms': 'tblGdXYo1onpkh7ow',
                 'schedules': 'tblDtGJOo2adZBWui', 'x-taxonomies': 'tbljWxEZPvYL3CmVU',
                 'physical_addresses': 'tblo9O05Tcxuhm5ro', 'contacts': 'tblX4DJEnxDCd3d6e'}

organizations_columns = ['id', 'name', 'alternate_name', 'description', 'email', 'website',
                         'tax_status', 'tax_id', 'year_incorporated', 'legal_status', 'logo',
                         'uri', 'parent_organization', 'funding', 'contacts', #'phones',
                         'locations', 'programs', 'organization_identifiers', 'attributes'
                         'metadata']

locations_columns = ["id", "location_type", "url", "organization_id", "name",
                "alternate_name", "description", "transportation", "latitude",
                "longitude", "external_identifier", "external_identifier_type",
                "languages", "addresses", "contacts", "accessibility", "phones",
                "schedules", "attributes", "metadata"]

services_columns = ["id", "organization_id", "program_id", "name", "alternate_name",
            "description", "url", "email", "status", "interpretation_services",
            "application_process", "fees_description", "wait_time", "fees",
            "accreditations", "eligibility_description", "minimum_age", "maximum_age",
            "assured_date", "assurer_email", "licenses", "alert", "last_modified",
            "service_areas", "service_at_locations", "languages",
            "organization", "funding", "cost_options", "program", "required_documents",
            "attributes", "metadata"]

services_at_location_columns = ['id', 'service_id', 'location_id', 'description',
                                'contacts', 'phones', 'schedules', 'location',
                                'attributes', 'metadata']

schedule_columns = ['id', 'service_id','location_id','service_at_location_id','valid_from', 'valid_to', 'dtstart',
                     'timezone', 'until',
                'count', 'wkst', 'freq', 'interval', 'byday', 'byweekno', 'bymonthday',
                'byyearday', 'description', 'opens_at', 'closes_at', 'schedule_link',
                'attending_type' ,'notes','attributes','metadata']


address_columns = ['id', 'attention', 'address_1', 'address_2', 'city', 'region',
                   'state_province', 'postal_code', 'country', 'address_type']

phones_columns = ['id', 'location_id', 'service_id', 'organization_id', 'contact_id', 'service_at_location_id', 'number', 'extension', 'type', 'description', 'languages', 'attributes', 'metadata']


taxonomy_terms_columns = ['id', 'code', 'name', 'description', 
                          'parent_id', 'taxonomy', 'taxonomy_detail', 'language', 
                          'taxonomy_id', 'term_uri', 'metadata']

taxonomy_columns = ['id', 'name', 'description', 'uri', 'version', 'metadata']

contact_columns = ['id', 'organization_id','service_id','service_at_location_id', 'location_id', 'name',
                    'title', 'department', 'email', 'phones','attributes','metadata']

schedule_columns = ['id', 'service_id', 'location_id', 'service_at_location_id' ,'valid_from', 'valid_to', 'dtstart',
                     'timezone', 'until',
                'count', 'wkst', 'freq', 'interval', 'byday', 'byweekno', 'bymonthday',
                'byyearday', 'description', 'opens_at', 'closes_at', 'schedule_link',
                'attending_type' , 'notes', 'attributes', 'metadata']

service_area_columns = ['id', 'service_id', 'name', 'description', 'extent',
                         'extent_type', 'uri', 'attributes', 'metadata']

