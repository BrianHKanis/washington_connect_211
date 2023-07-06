import requests
from ..src.api_export import topic_names
from ..settings import api_reader_root_url, api_writer_root_url

def test_reader_writer_match():
    table_names = topic_names
    for table_name in table_names:
        writer_url = api_writer_root_url + '/hsds3/' + table_name
        reader_url = api_reader_root_url + '/hsds3/' + table_name
        writer_records = requests.get(writer_url).json().sort(key=lambda x:x['id'])
        reader_records = requests.get(reader_url).json().sort(key=lambda x:x['id'])
        assert writer_records == reader_records