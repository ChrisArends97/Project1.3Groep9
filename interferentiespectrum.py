import sounddevice as sd
#import matplotlib.pyplot as plt
import numpy as np
from mijngeluid import fft_partitioned # zet mijngeluid.py in dezelfde folder als je notebook
import math
import pandas as pd
import time 
d = input("Type het totaal aantal punten in:") #input voor aantal metingen in de for-loop
for a in range(0,int(d)):

#print(sd.query_devices()) # geeft een lijst met devices en de bijbehorende nummers
    fs = 48000 
    duration = 5 #hoe lang er opgenomen wordt
    amp_ref = 0.0001
    arr = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64', device=1) # neemt op in de achtergrond
    Io = 1e-12

#print(arr.shape)
    sd.wait() #wachten met het opschrijven totdat alle data uit het opnemen er is
    gemiddelde = np.average(arr) #gemiddelde amplitude van de meting
    t = np.linspace(0, duration, int(fs*duration)) #tijd as
#plt.figure(dpi=100)
#plt.plot(t, arr, 'r-', ms=0.5, lw=0.5)
#plt.grid()
#plt.xlabel(r"Tijd $t$ [s]")
##plt.ylabel(r"Amplitude [a.u.]") # arbitrary units (we hebben niets gekalibreerd)
#plt.plot()
#print(gemiddelde)
    N = int(fs*duration) # Nsamples in signaal
    T = duration/N # Sampling tijd

    fhat = np.fft.fft(arr)
    x = np.linspace(0.0, 1.0/(2.0*T), N//2) # frequentie
    y = 2.0/N * np.abs(fhat[:N//2]) # Intensteit ||.||^2

#plt.figure(dpi=100)
#plt.plot(x,y, 'r-')
#plt.grid()
#plt.yscale("log")
#plt.xscale("log")
#plt.xlabel(r"Frequentie $f$ [Hz]")
#plt.ylabel(r"Intensiteit [a.u]")
#print(y)

    y1 = y.tolist() #intensiteit naar de lijst
#print(y1)
    y2 = [i[0] for i in y1] #dit zorgt er voor dat in de lijst [[],[]] de binneste [] verdwijnen

    y2 = np.array(y2) #vervolgens wordt er een array van gemaakt
    y2[y2==0]=1e-12 #alle 0 waardes worden met 1e-12 vervangen omdat dat gedefinieerd is als 0dB

    y3 = y2.tolist() #vervolgens is y3 een lijst van y2
    y4 = [] #lege lijst
    for I in y3:
        y4.append((10*(math.log(I/Io))) - 42.11) #de berekening van amplitude naar dB en dat in een nieuwe lijst
    


#plt.figure(dpi=100)
#plt.plot(x,y4, 'r-')
#plt.xlabel(r"Frequentie [Hz]")
#plt.ylabel(r"Db[a.u]")
#plt.grid()
#plt.show()

#plt.figure(dpi=100)


    df = fft_partitioned(arr[:,0], fs, t_tot=arr.shape[0]/fs, t_bin=1e-2) #mijn geluid programma

    b1 = df.t
    a1 = df.f


#plt.scatter(b1, a1, c=y4, cmap='cool', marker='.' ,s=1)
#plt.colorbar(label="Beta dB [a.u.]", norm=True)
#plt.xlabel("Tijd $s$ [s]")
#plt.ylim(1000,1005)
#ax = plt.axes()
#ax.set_facecolor("black")
#plt.ylabel("Frequentie $f$ [s]")
#plt.xlim(0,16)

#plt.show()

#voor 3d plot:
    

    gemiddelde = np.average(y4) #de gemiddelde dB van de meting
    print(gemiddelde)
    with open('datameting.txt','a') as f: #open het bestand datameting.txt en schrijf daar de gemiddelde dB op
        f.write(str(gemiddelde))
        f.write("\n")

        f.close() #bestand dicht
    print("Verplaats!") #verplaats de microfoon
    time.sleep(20)
    print("Tijd voorbij!") #meting begint weer
