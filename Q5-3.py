from G import G
import mysql.connector as mysql

conn = mysql.connect(host="mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     db = "cloud")
cursor = conn.cursor()
cursor.execute("SELECT * FROM  台灣股市 order by 日期")
rs = cursor.fetchall()
conn.close()
# for r in rs:
#     print(r)

conn = mysql.connect(host = G.host,
                     user = G.user,
                     password = G.password,
                     database = G.db)
cursor = conn.cursor()
data=[]
for r in rs :
    tmp = [str(r[1]),r[2],r[3],r[4],r[5]]
    data.append(tmp)
cmd = "insert into 台灣股市 (日期,最高,最低,開盤,收盤) values (%s,%s,%s,%s,%s)"
cursor.executemany(cmd,data)
conn.commit()
conn.close