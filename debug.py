from etl.extract_transform.src import airtable_client
from etl.extract_transform.src.build_tables import contacts

contacts_table = contacts.complete_table()

def find_lists(table, column_name):
    for record in table:
        if column_name in record.keys():
            if type(record[column_name]) == list:
                print(record)

find_lists(contacts_table, 'service_id')