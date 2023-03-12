from G import G
import mysql.connector as mysql
conn = mysql.connect(host = G.host,
                     user = G.user,
                     password = G.password,
                     database = G.db)
cursor = conn.cursor()
cmd = "delete from 員工資料表 where id = 1"
cursor.execute(cmd)
conn.commit()
cursor.execute("select * from 員工資料表")
rs = cursor.fetchall()
for r in rs :
    print(r)
conn.close