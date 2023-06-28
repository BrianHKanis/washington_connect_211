import hashlib
from ..airtable_client import build_dict, add_dpmgid
from ...data.hsds_columns import services_at_location_columns, locations_columns

required = ['id']

def add_keys_id(record, current, service_id):
    current['service_id'] = service_id
    current['location_id'] = record['id']
    current['id'] = hashlib.md5(((service_id + record['id'])).encode('utf-8')).hexdigest()

def build_record(record, service_at_locations_table):
    service_ids = record['service_ids']
    for service_id in service_ids: # Cycles through all service_ids per location
        current = {}
        add_keys_id(record, current, service_id)
        service_at_locations_table.append(current)
    return service_at_locations_table
        
def complete_table():
    service_at_locations_table = []
    locations_dict = build_dict('locations')
    for record in locations_dict:
        if 'service_ids' in record.keys():
            build_record(record, service_at_locations_table)
    return add_dpmgid(service_at_locations_table)