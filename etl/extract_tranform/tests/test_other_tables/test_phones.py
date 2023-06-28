from build_tables.other_tables import phones
from data.test_data.test_data_other_tables import phones_dict_test

def test_rename_columns():
    assert 'location_id' not in phones_dict_test[0].keys()
    assert 'location_ids' in phones_dict_test[0].keys()
    phones.rename_columns(phones_dict_test)
    assert 'location_id' in phones_dict_test[0].keys()

def test_delete_columns():
    assert "extra" in phones_dict_test[0].keys()
    phones.delete_columns(phones_dict_test)
    assert "extra" not in phones_dict_test[0].keys()

def test_add_required_if_missing():
    assert "number" not in phones_dict_test[0].keys()
    phones.add_required_if_missing(phones_dict_test)
    assert "number" in phones_dict_test[0].keys()

def test_complete_table():
    complete_table = phones.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict