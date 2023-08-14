import json, psycopg2
from psycopg2.extras import execute_values
from ...settings import LOCAL_DB_NAME, LOCAL_DB_USER, LOCAL_DB_PASSWORD
from ...settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

from console import merged  #For new import


topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']


# with open('whatcom.json', 'r') as f: #For quicker worflow rather than importing
    # table_data = json.load(f)
table_data = merged                #For new import

local_conn = psycopg2.connect(dbname=LOCAL_DB_NAME, user=LOCAL_DB_USER,
                              password=LOCAL_DB_PASSWORD)

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port=DB_PORT)


def insert_bulk(conn, table_name, table_data):
    cursor = conn.cursor()
    records = table_data[table_name]

    records_json = json.dumps(records)
    insert_query = f"""
    INSERT INTO {table_name} SELECT * FROM json_populate_recordset(null::{table_name}, %s);
    """
    cursor.execute(insert_query, (records_json,))
    conn.commit()
    return print(table_name + ' done')

def insert_all_bulk(topic_names, conn):
    for topic_name in topic_names:
        insert_bulk(conn, topic_name, table_data)
    print('Done All')









