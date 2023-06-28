from build_tables.core_tables import locations, organizations, service_at_location, services
from build_tables import hsds_columns, tables

organization_table = organizations.complete_table()
locations_table = locations.complete_table()
services_table = services.complete_table()
# service_at_location_table = service_at_location.complete_table()

def print_organizations():
    #Emails
    for org in organization_table:
        if 'email' in org.keys():
            print(org['email'])
    print('\n\n')
    #Websites
    for org in organization_table:
        if 'website' in org.keys():
            print(org['website'])
    print('\n\n')
    #Names
    for org in organization_table:
        if 'name' in org.keys():
            print(org['name'])
    print('\n\n')
    #Alternate_names
    for org in organization_table:
        if 'alternate_name' in org.keys():
            print(org['alternate_name'])
    #Description
    # for org in organization_table:
    #     if 'description' in org.keys():
    #         print(org['description'] + '\n')

def print_locations():
    #Names
    for loc in locations_table:
        if 'name' in loc.keys():
            print(loc['name'])
    print('\n\n')
    #Location Types
    # for loc in locations_table:
    #     if 'location_type' in loc.keys():
    #         print(loc['location_type'])


def print_services():
    #Application_processes
    for ser in services_table:
        if 'application_process' in ser.keys():
            print(ser['name'] + ser['application_process'] + '\n')
    print('\n\n')
    #Emails
    for ser in services_table:
        if 'email' in ser.keys():
            print(ser['email'])


# "application_process": "Online form available.",
#         "description": "Designed for children ages 0-6 and their adult(s). Wild Things is a placed-based community program that visits local parks each month to see what nature has to offer.",
#         "email": "communityprograms@wildwhatcom.org.",
#         "fees": "Suggested donations.",
#         "id": "reccaRSsso0aZKHH6",
#         "name": "Wild Things",