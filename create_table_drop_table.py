import sqlite3

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)

cursor = conn.cursor()

drop_table_query = "DROP TABLE IF EXISTS weather_newyork"
cursor.execute(drop_table_query)

create_table_query = "CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)"
cursor.execute(create_table_query)

conn.commit()

query = "SELECT name FROM sqlite_master WHERE type='table'"
cursor.execute(query)
tables = [ tup[0] for tup in cursor.fetchall() ]
print(f'tables: {tables}')

cursor.close()
conn.close()
