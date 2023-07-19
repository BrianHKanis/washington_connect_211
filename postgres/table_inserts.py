import json, psycopg2
# from console import merged

topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']

# tables = merged

# with open("mydata.json", "w") as final:
#    json.dump(tables, final)

with open('mydata.json', 'r') as f: #For quicker worflow rather than importing
    table_data = json.load(f)

# organizations = table_data['organization']

# def alter_table(table_name, column_name, data_type):
#     string = 'ALTER TABLE ' + table_name + '\n' 'ADD ' + column_name + ' ' + data_type + ';'
#     return string

conn = psycopg2.connect(dbname='hsds3_local', user='postgres')

def insert_into(table_name, conn):
    cursor = conn.cursor()
    columns = []
    records = table_data[table_name]
    for record in records:
        columns = list(record.keys())
        columns_string = ', '.join(columns)
        for k, v in record.items():
            if type(v) != int:
                if '"' in v:
                    record[k] = v.replace('"', "''")
                if "'" in v:
                    record[k] = v.replace("'", "''")
                if '\u200b' in v:
                    record[k] = v.replace('\u200b', '')
                if "'" in v:
                    record[k] = v.replace("'", "''") #Twice for services (Blue Skies Drivers)
        values = list(record.values())
        values_string = str(values).replace('[', '').replace(']', '').replace('"', "'")
        query = f'INSERT INTO {table_name} ({columns_string}) VALUES ({values_string})'
        cursor.execute(query)
        conn.commit()
    return print('done')

def insert_all(topic_names, conn):
    for topic_name in topic_names:
        insert_into(topic_name, conn)
        print(topic_name, 'Done')
    print('done')
    

def make_insert_into(table_name):
    columns = []
    records = table_data[table_name]
    for record in records:
        for key in record.keys():
            if key not in columns:
                columns.append(key)
    string1 = 'INSERT INTO ' + table_name + ' (' + (', '.join(columns)) + ') ' + 'VALUES' + '\n'
    string2 = ''
    for record in records:
        string2 += '('
        for column in columns:
            if column in record.keys():
                if type(record[column]) != int:
                    if '"' in record[column]:
                        record[column] = record[column].replace('"', "'")
                    string2 += '"' + record[column] + '"'
                else:
                    string2 += record[column]
            else:
                string2 += 'NULL'
            string2 += ', '
        string2 = string2[:-2]
        string2 += '),'
        string2 += '\n'
    string3 = string1 + string2[:-2] + ';'
    modified_string3 = string3.replace("'", "''")
    final = modified_string3.replace('"', "'")
    with open((table_name + '.sql'), 'w') as file:
        file.write(final)
        file.close()
    return final




#Create table SQL
# def create_tables():
#     for header in columns:
#         print(header + ' VARCHAR,')

# string1 = 'INSERT INTO ' + 'organization ' + '(' + (', '.join(columns)) + ') ' + 'VALUES'
# string2 = '('
# for organization in organizations:
#     for column in columns:
#         if column in organization.keys():
#             string2 += organization[column]
#         else:
#             string2 += 'NULL'
#         string2 += ', '
#     string2 = string2[:-2]
#     string2 += '),'
#     string2 += '\n'








#Insert into SQL
# for organization in organizations:
#     for v in organization.values():
#         if type(v) == list:
#             val = str(v)
#         else:
#             val = v
#         print(val)
#     print(')')
#     print('\n')








# with open('organizations.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(organizations)

# # Get CSV File Columns Name
# with open('csv_file_name.csv', 'r') as readObj:
#     csvReader = reader(readObj)
#     headers = next(csvReader)

# #To SQL table format
# for header in headers:
#     print(header + ' VARCHAR,')

# # Column names with space and comma
# for header in headers:
#     print(header, end=', ')

# print(headers)