from postgres.table_inserts import insert_all, topic_names, conn, table_data

insert_all(topic_names, conn)