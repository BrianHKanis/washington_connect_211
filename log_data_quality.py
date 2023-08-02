import json
import pandas as pd

# from console import merged
# table_data = merged

with open('whatcom.json', 'r') as f: #For quicker worflow rather than importing
    table_data = json.load(f)

# CHECK ---> '\\xa0'

topic_names = ['organization', 'location', 'service', 'service_at_location',
        'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']

poor_data = {'spaces': [], 'non_breaking_space': [],
             'width_space': [], 'newline': [],
             'double_quotes': [], 'non_castable': [],
             'semi_colons': [], 'single_quotes': []}



def append_to_log(defect_type, table_name, record, v):
    if 'source_id' in record.keys():
        data_dict = {'table_name': table_name, 'id': record['id'], 'source_id': record['source_id'], 'value': v}
        poor_data[defect_type].append(data_dict)
    else:
        data_dict = {'table_name': table_name, 'id': record['id'], 'value': v}
        poor_data[defect_type].append(data_dict)

def find_spaces(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if len(v) > 0:
                    if v[0] == ' ':
                        append_to_log('spaces', table_name, record, v)

def find_non_breaking_space(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if '\u00a0' in v:
                    append_to_log('non_breaking_space', table_name, record, v)

def find_width_space(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if '\u200b' in v:
                    append_to_log('width_space', table_name, record, v)

def find_newline(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if '\n' in v:
                    if 'source_id' in record.keys():
                        append_to_log('newline', table_name, record, v)

def find_double_quotes(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if '"' in v:
                    append_to_log('double_quotes', table_name, record, v)

def find_cannot_be_casted(table_name):
    table = table_data[table_name]
    for record in table:
        if 'interval' in record.keys():
            v = record['interval']
            if type(v) != int:
                append_to_log('non_castable', table_name, record, v)

def find_semi_colons(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if ';' in v:
                    append_to_log('semi_colons', table_name, record, v)

def find_single_quotes_chars(table_name):
    table = table_data[table_name]
    for record in table:
        for v in record.values():
            if type(v) == str:
                if '\u2019' in v:
                    append_to_log('single_quotes', table_name, record, v)
#########################
def list_all_columns(table_name):
    table = table_data[table_name]
    table_columns = []
    for record in table:
        for k in record.keys():
            if k not in table_columns:
                table_columns.append(k)
    print(table_columns)

def print_column(table_name, column_name):
    table = table_data[table_name]
    for record in table:
        if column_name in record.keys():
            print(record[column_name])

def print_column_and_type(table_name, column_name):
    table = table_data[table_name]
    for record in table:
        if column_name in record.keys():
            print(record[column_name], type(record[column_name]))

def find_all_per_table(table_name):
    find_spaces(table_name)
    find_non_breaking_space(table_name)
    find_width_space(table_name)
    find_newline(table_name)
    find_cannot_be_casted(table_name)
    find_double_quotes(table_name)
    find_semi_colons(table_name)
    find_single_quotes_chars(table_name)
    
def find_all():
    for table in topic_names:
        find_all_per_table(table)


find_all()

with open("z_quality_check.json", "w") as final:
   json.dump(poor_data, final, indent=4)