import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

#lijsten
x = []
y = []
z = []
waarde = []


#het inlezen van de 0,1 en 2de colom in het tekstbestand met de coordinaten
#het inlezen van het tekstbestand met de meting
datax = np.loadtxt("lokaal.txt",usecols=0,skiprows =0,dtype = 'float',encoding=None,delimiter=",") 
for a in datax:
    x.append(a)
datax = np.loadtxt("lokaal.txt",usecols=1,skiprows =0,dtype = 'float',encoding=None,delimiter=",")
for a in datax:
    y.append(a)    
datax = np.loadtxt("lokaal.txt",usecols=2,skiprows =0,dtype = 'float',encoding=None,delimiter=",")
for a in datax:
    z.append(a)
datax = np.loadtxt("datametinghoogte1.30.txt",usecols=0,skiprows =0,dtype = 'float',encoding=None,delimiter=",")
for a in datax:
    waarde.append(a)

fig = plt.figure()
ax = plt.axes(projection="3d") #leeg 3d canvas
plt.title("Lokaal 3e verdieping bij f = 440 Hz hoogte=1.30m met nagalmtijd")
plt.xlabel("Lengte(m)")
plt.ylabel("Breedte(m)")
ax.set_zlim(0,2.50)
ax.set_zlabel("Hoogte(m)")
ax.text(0, 0, 1.30, "1.66s", color='black')
ax.text(2, 1, 1.30, "1.63s", color='black')
ax.text(5, 1, 1.30, "1.07s", color='black')
im = ax.scatter(x,y,z,c=waarde,s=750,cmap='Reds', depthshade=False) #het plotten van de arrays uit de tekstbestand
a = fig.colorbar(im)
ax.view_init(270, -90)
a.ax.set_ylabel("Gemeten dB")

plt.show()
