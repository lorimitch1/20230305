import numpy as np

from G import G
import mysql.connector as mysql
import pylab as plt

conn = mysql.connect(host="mahaljsp.asuscomm.com",
                     user = "lcc",
                     password = "lcc0507",
                     db = "cloud")
cursor = conn.cursor()
cursor.execute("SELECT * FROM 台銀黃金 where  日期 > '2020-01-01' ORDER BY 日期 ")
rs = cursor.fetchall()
y = [r[3] for r in rs]
x= list (range(len(y)))
plt.plot(x,y)
f = np.poly1d(np.polyfit(x,y,10))
plt.plot(x, f(x), c= 'red')
plt.show()