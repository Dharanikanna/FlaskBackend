import os
from dotenv import load_dotenv
import psycopg2
import psycopg2.extras

load_dotenv()

DB_NAME = os.getenv('db')
DB_USER = os.getenv('user')
DB_PASS = os.getenv('password')
DB_HOST = os.getenv('host')

# print(DB_NAME,DB_HOST,DB_PASS,DB_USER)

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# print(conn.dsn)
# print(len(conn.dsn))

connection_test = ("user="+str(DB_USER)+" password=xxx dbname="+str(DB_NAME)+" host="+str(DB_HOST))
# print(connection_test)
# print(len(connection_test))

if conn.dsn == (connection_test):
    print("Database status : Database connected successfully")
else:
    print("Database status : Database not connected")

# with conn:
#     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

#         cur.execute("SELECT * FROM users;")
#         print(cur.fetchall())

# # conn.close()

query = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)