
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from mijngeluid import fft_partitioned 
import math
import time
#df = fft_partitioned(arr[:,0], fs, t_tot=arr.shape[0]/fs, t_bin=1e-2)
File_dataa1 = np.loadtxt("varfx5y1.txt",usecols=0,dtype=float,encoding=None) #via numpy de txt bestanden inlezen en die in een array zetten
File_datab1 = np.loadtxt("vartx5y1.txt",usecols=0,dtype=float,encoding=None)
File_datay4 = np.loadtxt("vary4x5y1.txt",usecols=0,dtype=float,encoding=None)


plt.scatter(File_datab1, File_dataa1, c=File_datay4, cmap='seismic', marker='.' ,s=1, vmin=0) #het plotten van de punten in de array's 
plt.colorbar(label="Beta dB [a.u.]", norm=True)
plt.xlabel("Tijd $s$ [s]")
plt.ylim(20,20000) #ylimiet
ax = plt.axes()
ax.set_facecolor("black")
plt.ylabel("Frequentie $f$ [s]")
plt.xlim(0,170) #xlimiet
plt.title("X5 Y1")
plt.show()