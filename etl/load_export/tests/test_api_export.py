import requests
from ..src.api_export import topic_names

def test_reader_writer_match():
    table_names = topic_names
    for table_name in table_names:
        writer_url = 'http://128.199.8.15:81/hsds3/' + table_name
        reader_url = 'http://128.199.8.15:82/hsds3/' + table_name
        writer_records = requests.get(writer_url).json().sort(key=lambda x:x['id'])
        reader_records = requests.get(reader_url).json().sort(key=lambda x:x['id'])
        assert writer_records == reader_records