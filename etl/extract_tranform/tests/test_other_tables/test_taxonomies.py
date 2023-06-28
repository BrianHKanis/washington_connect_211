from build_tables.other_tables import taxonomies
from data.test_data.test_data_other_tables import taxonomies_dict_test

def test_rename_keys():
    assert "term" in taxonomies_dict_test[0].keys()
    taxonomies.rename_columns(taxonomies_dict_test)
    assert "name" in taxonomies_dict_test[0].keys()

def test_delete_columns():
    assert "extra" in taxonomies_dict_test[0].keys()
    taxonomies.delete_columns(taxonomies_dict_test)
    assert "extra" not in taxonomies_dict_test[0].keys()
    assert "term" not in taxonomies_dict_test[0].keys()

def test_add_required_if_missing():
    assert "id" not in taxonomies_dict_test[0].keys()
    taxonomies.add_required_if_missing(taxonomies_dict_test)
    assert "id" in taxonomies_dict_test[0].keys()

def test_complete_table():
    complete_table = taxonomies.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict