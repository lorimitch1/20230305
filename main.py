from G import G
import mysql.connector as mysql

conn = mysql.connect(host = G.host,
                     user = G.user,
                     password = G.password,
                     database = G.db)
cursor = conn.cursor()
cmd = "select * from 台灣股市 "
cursor.execute(cmd)
rs = cursor.fetchall()
conn.close()

for r in rs :
    print(r)