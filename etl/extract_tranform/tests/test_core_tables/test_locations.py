from build_tables.core_tables import locations
from data.test_data.test_data_core_tables import location_dict_test

def test_rename_columns():
    assert 'schedules' not in location_dict_test[0].keys()
    locations.rename_columns(location_dict_test)
    assert 'schedules' in location_dict_test[0].keys()

def test_delete_columns():
    assert 'extra' in location_dict_test[0].keys()
    locations.delete_columns(location_dict_test)
    assert 'extra' not in location_dict_test[0].keys()

def test_add_required_if_missing():
    assert 'location_type' not in location_dict_test[0].keys()
    locations.add_required_if_missing(location_dict_test)
    assert 'location_type' in location_dict_test[0].keys()

def test_complete_table():
    complete_table = locations.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict