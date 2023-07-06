# import requests

# topic_names = ['organization', 'location', 'service', 'service_at_location',
#         'contact', 'schedule', 'phone', 'taxonomy', 'taxonomy_term']

# org_writer = 'http://128.199.8.15:81/hsds3/contact'
# org_reader = 'http://128.199.8.15:82/hsds3/contact'

# writer_response = requests.get(org_writer)
# writer_records = writer_response.json()

# reader_response = requests.get(org_reader)
# reader_records = reader_response.json()


# print(reader_records == writer_records)

# true_copies = ['organization', 'taxonomy_term']

# def get_columns(records):
#     columns = []
#     for record in records:
#         for key in record.keys():
#             if key not in columns:
#                 columns.append(key)
#     return columns

# def sort_records(records):
#     sorted_records = sorted(records, key = lambda x:x['id'])
#     return sorted_records