import pylab as plt
import numpy as np
n=100
np.random.seed(0)
x= np.linspace(0,n,n+1)
y= 0.5*x+10+np.random.randint(-100,100,n+1)

# plt.xlim(0,10)
# plt.ylim(0,20)
plt.scatter(x,y ,)

# args= np.polyfit(x,y,1)
# r = args[0]*x+args[1]
args = np.polyfit(x,y,2)
r = args[0]*pow(x,2)+args[1]*x+args[2]
#f= np.poly1d(args)
f= np.poly1d(np.polyfit(x,y,10))
plt.plot(x,f(x))
plt.show()