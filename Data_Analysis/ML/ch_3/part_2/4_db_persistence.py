import pandas as pd

import sqlite3 #pymysql <- 설치

conn = sqlite3.connect("./data/flights.db")
cur = conn.cursor()
cur.execute("select * from airlines limit 5;")
results = cur.fetchall()

df_airplines = pd.read_sql_query("select * from airlines;", conn)
df_airplines



df_airports = pd.read_sql_query("select * from airports;", conn)
df_routes = pd.read_sql_query("select * from routes;", conn)



df_airports.head()

df_routes.head()





writer = pd.ExcelWriter('./data/df_routes.xlsx', engine='xlsxwriter')
df_routes.to_excel(writer, sheet_name='Sheet1')
df_routes.to_pickle("./data/df_routes.pickle")
df_routes_pickle = pd.read_pickle("./data/df_routes.pickle")
df_routes_pickle.head()


df_routes_pickle.describe()