from scipy.interpolate import lagrange
from numpy import *
import matplotlib.pyplot as plt
def jop(x):
    return 4*x**3-15*x-3
x = array([-2,0,1,2],dtype = float)
y = array([-11,-3,-11,5],dtype = float)
U = array([1.5,-0.5,0.5,2.5])

def L(x,y,k):
    summa=0
    for g in range (len(y)):
        p1=1
        p2=1
        for i in range (len(y)):
            if i ==g:
                p1 *= 1
                p2 *= 1
            else:
                p1*=(k-x[i])
                p2*=(x[g]-x[i])
        summa += y[g]*p1/p2
    return summa
xnew = linspace (min(x),max(x))
ynew = [L(x,y,i) for i in xnew]
plt.plot(x,y,'o',xnew,ynew)
plt.title('LB_7 Yevheniy Horoshchenko')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
