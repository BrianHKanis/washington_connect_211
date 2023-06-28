from build_tables.core_tables import service_at_location
from build_tables.tables import build_dict
from data.test_data.test_data_core_tables import service_dict_test

location_dict_test = [{"id": "rec1OU4skk8AJwaLa",
                    "name": "Compass Health Whatcom WISe Office",
                    "schedule": "",
                    "extra": "",
                    "service_ids": ["rec1OU4skk8AJwaLa"]}, {'id': '1'}]

def test_build_record():
    services_dict = service_dict_test
    locations_dict = location_dict_test

    record = locations_dict[0]
    service_at_locations_table = []
    service_at_location.build_record(record, service_at_locations_table)
    assert service_at_locations_table == [{'service_id': 'rec1OU4skk8AJwaLa', 'location_id': 'rec1OU4skk8AJwaLa', 'id': '56869a6ed345e9392fca715d1f79cfbd'}]

def test_complete_table():
    complete_table = service_at_location.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict

def test_unique_ids():
    complete_table = service_at_location.complete_table()
    list_of_ids = [record['id'] for record in complete_table]
    assert len(list_of_ids) == len(set(list_of_ids))