import json
from etl.load_export.src.postgres_export.table_inserts import topic_names, local_conn, conn, insert_all_bulk
from etl.load_export.src.postgres_export.log_data_quality import find_all_cannot_be_casted

find_all_cannot_be_casted()
insert_all_bulk(topic_names, local_conn)




























cursor = local_conn.cursor()
query = "SELECT * FROM organization LIMIT 5;"
cursor.execute(query)
results = cursor.fetchall()
