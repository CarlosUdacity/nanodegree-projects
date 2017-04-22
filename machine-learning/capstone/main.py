from sqlalchemy import create_engine
import pandas as pd
import json

with open('db_connection.json') as data_file:
    p = json.load(data_file)

conn_str = "postgresql://" + p["user"] + ":" + p["password"] + \
           "@" + p["netloc"] + ":" + str(p["port"]) + "/" + p["dbname"]
engine = create_engine(conn_str)

a = pd.read_sql_query('SELECT count(DISTINCT id) FROM auth_user', con=engine)

print(a)