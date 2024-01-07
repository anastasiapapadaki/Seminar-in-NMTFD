import numpy as np
import matplotlib.pylab as plt


line4 = np.loadtxt('velocity-line-x=4.txt')
line6 = np.loadtxt('velocity-line-x=6.txt')
line10 = np.loadtxt('velocity-line-x=10.txt')
line19 = np.loadtxt('velocity-line-x=19.txt')

plt.figure(figsize=(9,6))
plt.plot(line4[:,1]/0.005117, line4[:,0], 'r--' , LineWidth = 2)
plt.plot(0.5+line6[:,1]/0.005117, line6[:,0], 'b--' , LineWidth = 2)
plt.plot(1+line10[:,1]/0.005117, line10[:,0], 'y--' , LineWidth = 2)
plt.plot(1.5+line19[:,1]/0.005117, line19[:,0], 'p--' , LineWidth = 2)
plt.xlabel("U/Uo",fontsize=22,) 
plt.ylabel("y/h",fontsize=22)

plt.xticks(fontsize=16);  plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))

#$plt.tight_layout()



plt.title('Velocity Line',fontweight="bold")
plt.legend(['line-x=4','line-x=6','line-x=10','line-x=19'])
plt.show()
