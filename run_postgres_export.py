import json
from etl.load_export.src.postgres_export.table_inserts import insert_all, topic_names, local_conn, conn, clean_data, clean_record, clean_all, clean_table, export_clean, insert_bulk, insert_all_bulk

clean_all(topic_names)
export_clean(clean_data)

with open('whatcom_clean.json', 'r') as f:
    clean_data = json.load(f)

insert_all_bulk(topic_names, local_conn, table_data=clean_data)

# insert_all(topic_names, conn)

# cursor = local_conn.cursor()
# query = "SELECT * FROM organization LIMIT 5;"
# cursor.execute(query)
# results = cursor.fetchall()
