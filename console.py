import requests, json, time
from etl.load_export.settings import api_writer_root_url
from etl.extract_transform.src.build_tables import organizations, locations, services, service_at_locations, contacts, schedules, phones, taxonomy_terms, taxonomies
topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']

def load_all_tables():
    print("Building Organizations...")
    organizations_table = organizations.complete_table()
    print("Building Locations...")
    locations_table = locations.complete_table()
    print("Building Services...")
    services_table = services.complete_table()
    print("Building Service at Location...")
    service_at_locations_table = service_at_locations.complete_table()
    print("Building Contacts...")
    contacts_table = contacts.complete_table()
    print("Building Schedules...")
    schedules_table = schedules.complete_table()
    print("Building Phones...")
    phones_table = phones.complete_table()
    print("Building Taxonomy Terms...")
    taxonomy_terms_table = taxonomy_terms.complete_table()
    print("Building Taxonomies...")
    taxonomies_table = taxonomies.complete_table()
    files = [organizations_table, locations_table, services_table, service_at_locations_table,
        contacts_table, schedules_table, phones_table, taxonomies_table, taxonomy_terms_table]
    return files

def merge_endpoints(all_tables, topic_names):
    files = all_tables
    endpoints = topic_names
    merged = dict(zip(endpoints, files))
    return merged

def export_files(merged, root_url):
    for k, v in merged.items():
        url = root_url + str('/hsds3/') + str(k)
        status = requests.put(url, json.dumps(v))
        print((str(k) + ': ' + (str(status))).rjust(40, ' '))
    return print('Done Exporting')

def find_lists(records, key_name):
    for record in records:
        if key_name in record.keys():
            if type(record[key_name]) == list:
                print(record)

start_time = time.time()
all_tables = load_all_tables()
print('Tables Loaded')
print()
merged = merge_endpoints(all_tables, topic_names)

# print('Endpoints paired with coresponding table')
# print()
# print('Exporting...')
# export_files(merged, api_writer_root_url)
# end_time = time.time()
# print()
# print('Total Time: ' + str(round(end_time-start_time, 5)) + ' seconds')




