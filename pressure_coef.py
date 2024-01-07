import numpy as np
import matplotlib.pylab as plt
from math import e

p0=-3,19*e**(-0.3)
rho= 998,2
U_0=0.005117

def Cp(p,p0,rho,U0):
    return (p-p0)/(0.5*rho*U0^2)

data = np.loadtxt('pressure_coefficient.txt')
x=data[:,0]
p= data[:,1]
plt.figure(figsize=(9,6))

plt.plot(x,p, 'r--' , LineWidth = 2)
plt.xlabel("Position",fontsize=22,) 
plt.ylabel("Cp",fontsize=22)

plt.xticks(fontsize=16);  plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))

plt.tight_layout()



plt.title('Static Pressure',fontweight="bold")
plt.legend(['Static Pressure'])
plt.show()
