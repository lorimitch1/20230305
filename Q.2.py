from G import G
import mysql.connector as mysql

conn = mysql.connect(host = G.host,
                     user = G.user,
                     password = G.password,
                     database = G.db)
cursor = conn.cursor()
cmd = "insert into 台灣股市 (日期,開盤,最高,最低,收盤) values (2023/3/3,15621.36,15713.42,15606.85,15608.42)"
cursor.execute(cmd)
conn.commit()
conn.close()