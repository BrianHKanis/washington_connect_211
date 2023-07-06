from ..src.airtable_client import headers, table_id_dict, make_request, rename_columns, delete_columns, duplicate_record_if_multiple_foreign_keys, add_required_if_missing

data_for_testing = [{"id": "1", "name": "Test Name", "description": "test_description", "url": "http://......", "extra": "extra_value", "dpmgid": "69", "organization_id": ['1', '2', '3']}, {"id": "2", "name": "Test Name 2", "description": "test_description2", "url": "http://......2", "extra": "extra_value", "location_id": ['A', 'B', 'C']}]
required_keys = ['id', 'name', 'description', 'required', 'dpmgid', ]
columns_for_testing = ['id', 'name', 'description', 'url', 'organization_id', 'location_id']
columns_to_rename = {'url': 'website'}
columns_to_duplicate = ['organization_id', 'location_id']

def test_make_requests():
    responses = []
    table_keys = table_id_dict.keys()
    for key in table_keys:
        response = make_request(key)
        responses.append(response.status_code)
    assert set(responses) == {200}

def test_rename_columns():
    assert 'url' in data_for_testing[0].keys()
    assert 'website' not in data_for_testing[0].keys()
    rename_columns(data_for_testing, columns_to_rename)
    assert 'website' in data_for_testing[0].keys()

def test_delete_columns():
    assert 'extra' in data_for_testing[0].keys()
    delete_columns(data_for_testing, columns_for_testing)
    assert 'extra' not in data_for_testing[0].keys()

def test_add_required_if_missing():
    assert 'required' not in data_for_testing[0].keys()
    add_required_if_missing(data_for_testing, required_keys)
    assert 'required' in data_for_testing[0]

def test_duplicate_record_if_multiple_foreign_keys():
    assert len(data_for_testing) == 2
    duplicate_record_if_multiple_foreign_keys(data_for_testing, columns_to_duplicate)
    duplicate_record_if_multiple_foreign_keys(data_for_testing, columns_to_duplicate)
    assert len(data_for_testing) == 6

