import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',
                        password='admin')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE tracks_demo")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)