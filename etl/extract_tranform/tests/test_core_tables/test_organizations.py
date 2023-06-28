from build_tables.core_tables import organizations
from data.test_data.test_data_core_tables import organization_dict_test

def test_rename_columns():
    assert 'website' not in organization_dict_test[0].keys()
    organizations.rename_columns(organization_dict_test)
    assert 'website' in organization_dict_test[0].keys()

def test_delete_columns():
    assert 'extra' in organization_dict_test[0].keys()
    organizations.delete_columns(organization_dict_test)
    assert 'extra' not in organization_dict_test[0].keys()

def test_add_required_if_missing():
    assert 'description' not in organization_dict_test[0].keys()
    organizations.add_required_if_missing(organization_dict_test)
    assert 'description' in organization_dict_test[0].keys()

def test_complete_table():
    complete_table = organizations.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict