import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt('yplus_lowerwall.txt')

plt.figure(figsize=(9,6))
plt.plot(data[:,0], data[:,1], 'r--' , LineWidth = 2)
plt.xlabel("Position",fontsize=22,) 
plt.ylabel("Wall Yplus",fontsize=22)

plt.xticks(fontsize=16);  plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))

plt.tight_layout()



plt.title('Wall Yplus',fontweight="bold")
plt.legend(['Wall Yplus'])
plt.show()
