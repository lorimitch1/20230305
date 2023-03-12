from G import G
import mysql.connector as mysql

conn = mysql.connect(host="mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     db = "cloud")
cursor = conn.cursor()
cursor.execute("SELECT * FROM 台灣股市 ORDER BY 日期 ")
rs = cursor.fetchall()
conn.close()


conn = mysql.connect(host = G.host,
                     user = G.user,
                     password = G.password,
                     database = G.db)
cursor = conn.cursor()
for r in rs :
    cmd = f"insert into 台灣股市 (日期,開盤,最高,最低,收盤) values ('{str(r[1])}','{r[2]}','{r[3]}','{r[4]}','{r[5]}')"
    print(cmd)
    cursor.execute(cmd)
conn.commit()