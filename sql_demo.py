from postgres.sql_stuff import insert_all, topic_names, conn, table_data

insert_all(topic_names, conn)