import mysql.connector as mysql
from mysql.connector import Error

from convert_top_tracks import trackdata

try:
    conn = mysql.connect(host='localhost', database='tracks_demo', user='root', password='admin')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS track_info;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE track_info(id int, artist varchar(255),artist_url varchar(255), song varchar(255),song_url varchar(255), duration_ms varchar(255), explicit varchar(255), album varchar(255), popularity varchar(255))")
        print("Table is created....")
        #loop through the data frame
        for i,row in trackdata.iterrows():
            #here %S means string values
            sql = "INSERT INTO tracks_demo.track_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)