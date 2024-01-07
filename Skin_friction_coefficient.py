import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt('skin_Friction_Coefficient.txt')

plt.figure(figsize=(9,6))
plt.plot(data[:,0], data[:,1], 'r--' , LineWidth = 2)
plt.xlabel("Position",fontsize=22,) 
plt.ylabel("Skin_Friction_Coefficient",fontsize=22)

plt.xticks(fontsize=16);  plt.yticks(fontsize=16)
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 4))

plt.tight_layout()



plt.title('Skin_Friction_Coefficient',fontweight="bold")
plt.legend(['Skin_Friction_Coefficient'])
plt.show()
