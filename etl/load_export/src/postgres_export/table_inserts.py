import json, psycopg2
from psycopg2.extras import execute_values
from ...settings import LOCAL_DB_NAME, LOCAL_DB_USER, LOCAL_DB_PASSWORD
from ...settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from ...data.topic_columns import topic_keys

# from console import merged  #For new import


topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']


with open('whatcom.json', 'r') as f: #For quicker worflow rather than importing
    table_data = json.load(f)
# table_data = merged                #For new import

local_conn = psycopg2.connect(dbname=LOCAL_DB_NAME, user=LOCAL_DB_USER,
                              password=LOCAL_DB_PASSWORD)

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port=DB_PORT)

# To see records locally before exporting to DB
clean_data = {'organization': [], 'location': [], 'service': [], 'service_at_location': [],
        'contact': [], 'schedule': [], 'phone': [], 'taxonomy': [], 'taxonomy_term': []}

def clean_record(record):
    for k, v in record.items():
        if type(v) == str:
            #Necessary for database insertion with normal f'string
            if '"' in v:
                record[k] = v.replace('"', "''")
            if "'" in v:
                record[k] = v.replace("'", "''")
            if "'" in v:
                record[k] = v.replace("'", "''") #Twice for services (Blue Skies Drivers)
            #Additional data cleansing
            if len(v) > 1:
                if v[0] == ' ':
                    record[k] = v[1:]
            if '\u00a0' in v:
                record[k] = v.replace('\u00a0', '')
            if '\u200b' in v:
                record[k] = v.replace('\u200b', '')
            if '\n' in v:
                record[k] = v.replace('\n', ' ')
    return record

def clean_table(table_name):
    records = table_data[table_name]
    for record in records:
        clean_record(record)
        clean_data[table_name].append(record)

def clean_all(topic_names):
    for topic_name in topic_names:
        clean_table(topic_name)

def export_clean(clean_data):
    with open("whatcom_clean.json", "w") as final:
        json.dump(clean_data, final, indent=4)

##INSERT ALL BULK
def insert_bulk(conn, table_name, table_data=table_data):
    cursor = conn.cursor()
    records = table_data[table_name]
    records_json = json.dumps(records)
    insert_query = f"""
    INSERT INTO {table_name} SELECT * FROM json_populate_recordset(null::{table_name}, %s);
    """
    cursor.execute(insert_query, (records_json,))
    conn.commit()
    return print(table_name + ' done')

def insert_all_bulk(topic_names, conn, table_data=table_data):
    for topic_name in topic_names:
        insert_bulk(conn, topic_name, table_data=table_data)
    print('Done All')







# def insert_into(table_name, conn):
#     cursor = conn.cursor()
#     columns = []
#     records = table_data[table_name]
#     for record in records:
#         columns = list(record.keys())
#         columns_string = ', '.join(columns)
#         cleaned_record = clean_record(record)
#         values = list(cleaned_record.values())
#         values_string = str(values).replace('[', '').replace(']', '').replace('"', "'")
#         query = f'INSERT INTO {table_name} ({columns_string}) VALUES ({values_string})'
#         cursor.execute(query)
#         conn.commit()
#     return print(table_name, 'done')

# def insert_all(topic_names, conn):
#     for topic_name in topic_names:
#         topic_name
#         insert_into(topic_name, conn)
#     print('Done All')


# def make_insert_into(table_name):
#     columns = []
#     records = table_data[table_name]
#     for record in records:
#         for key in record.keys():
#             if key not in columns:
#                 columns.append(key)
#     string1 = 'INSERT INTO ' + table_name + ' (' + (', '.join(columns)) + ') ' + 'VALUES' + '\n'
#     string2 = ''
#     for record in records:
#         string2 += '('
#         for column in columns:
#             if column in record.keys():
#                 if type(record[column]) != int:
#                     if '"' in record[column]:
#                         record[column] = record[column].replace('"', "'")
#                     string2 += '"' + record[column] + '"'
#                 else:
#                     string2 += record[column]
#             else:
#                 string2 += 'NULL'
#             string2 += ', '
#         string2 = string2[:-2]
#         string2 += '),'
#         string2 += '\n'
#     string3 = string1 + string2[:-2] + ';'
#     modified_string3 = string3.replace("'", "''")
#     final = modified_string3.replace('"', "'")
#     with open((table_name + '.sql'), 'w') as file:
#         file.write(final)
#         file.close()
#     return final