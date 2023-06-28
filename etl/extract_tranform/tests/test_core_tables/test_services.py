from build_tables.core_tables import services
from data.test_data.test_data_core_tables import service_dict_test

def test_rename_columns():
    assert 'schedules' not in service_dict_test[0].keys()
    services.rename_columns(service_dict_test)
    assert 'schedules' in service_dict_test[0].keys()

def test_delete_columns():
    assert 'extra' in service_dict_test[0].keys()
    services.delete_columns(service_dict_test)
    assert 'extra' not in service_dict_test[0].keys()

def test_add_required_if_missing():
    assert 'status' not in service_dict_test[0].keys()
    services.add_required_if_missing(service_dict_test)
    assert 'status' in service_dict_test[0].keys()

def test_complete_table():
    complete_table = services.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict