from build_tables import tables

def test_make_request():
    response = tables.make_request('services')
    assert response.status_code == 200

def test_make_multiple_requests():
    responses = [tables.make_request(key).status_code for key in tables.table_id_dict.keys()]
    assert responses == [200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

def test_get_next_url():
    url = 'https://api.airtable.com/v0/appqiHo29pLLU6RDC/tblqoitqeXyTPwU8i'
    records_json = tables.make_request('organizations').json()
    next_url = tables.get_next_url(url, records_json)
    assert len(url) == 63
    assert len(next_url) == 107

def test_add_pages():
    url = 'https://api.airtable.com/v0/appqiHo29pLLU6RDC/tblqoitqeXyTPwU8i'
    records_json = tables.make_request('organizations').json()
    next_url = tables.get_next_url(url, records_json)
    records_list = []
    tables.add_pages(url, next_url, records_list)
    assert len(records_list) > 1

def test_build_dict():
    services_dict = tables.build_dict('services')
    assert type(services_dict) == list
    assert type(services_dict[0]) == dict