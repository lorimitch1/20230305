from G import G
import mysql.connector as mysql

conn = mysql.connect(host="mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     db = "cloud")
cursor = conn.cursor()
cursor.execute("SELECT * FROM 台銀黃金 ORDER BY 日期 ")
rs = cursor.fetchall()
for r in rs :
    print(r)
