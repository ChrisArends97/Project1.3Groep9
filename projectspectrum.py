import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from mijngeluid import fft_partitioned 
import math
import pandas as pd
de = input("Hoe lang wilt u totaal meten in seconden?:") #input voor de duratie van de meting
xcor= float(input("X-coordinaat:")) 
ycor= float(input("Y-coordinaat:"))
zcor= float(input("Z-coordinaat:"))
print(sd.query_devices())
fs = 48000 
duration = int(de)
amp_ref = 0.0001
arr = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64', device=1) # neemt op in de achtergrond
Io = 1e-12

print(arr.shape)
sd.wait()
gemiddelde = np.average(arr)
t = np.linspace(0, duration, int(fs*duration)) # tijd as

#print(gemiddelde)
N = int(fs*duration) # Nsamples in signaal
T = duration/N # Sampling tijd

fhat = np.fft.fft(arr)
x = np.linspace(0.0, 1.0/(2.0*T), N//2) # frequentie
y = 2.0/N * np.abs(fhat[:N//2]) # Intensteit ||.||^2

y1 = y.tolist()
#print(y1)
y2 = [i[0] for i in y1]

y2 = np.array(y2)
y2[y2==0]=1e-12

y3 = y2.tolist()
y4 = []
for I in y3:
    y4.append((10*(math.log(I/Io))) - 42.11)
    


#alle waardes die gevonden worden voor het spectogram opschrijven in losse txt zodat ze via lezenvanspectrum.py 
#weer ingelezen kunnen worden 

df = fft_partitioned(arr[:,0], fs, t_tot=arr.shape[0]/fs, t_bin=1e-2)
with open(str(xcor) + str(ycor) + str(zcor) +  'vart.txt','w') as f3: #maak een txt bestand met coordinaat naam en schrijf de waarde op
    for a in df.t:

        f3.write(str(a))
        f3.write("\n")

    f3.close()
with open(str(xcor) + str(ycor) + str(zcor) + 'vartnormaal.txt','w') as f6:
    for a in t:

        f6.write(str(a))
        f6.write("\n")

    f6.close()

with open(str(xcor) + str(ycor) + str(zcor) + 'varf.txt','w') as f2:
    for a in df.f:

        f2.write(str(a))
        f2.write("\n")

    f2.close()
with open(str(xcor) + str(ycor) + str(zcor) + 'vary4.txt','w') as f4:
    for a in y4:

        f4.write(str(a))
        f4.write("\n")

    f4.close()


b1 = df.t
a1 = df.f

    

