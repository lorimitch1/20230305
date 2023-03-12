from G import G
import mysql.connector as mysql
import pylab as plt

conn = mysql.connect(host="mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     db = "cloud")
cursor = conn.cursor()
cursor.execute("SELECT * FROM 台銀黃金 ORDER BY 日期 ")
rs = cursor.fetchall()
y = [r[3] for r in rs]
x= list (range(len(y)))
plt.plot(x,y)
plt.show()