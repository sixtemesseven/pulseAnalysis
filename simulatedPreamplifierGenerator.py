# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:57:05 2019

@author: justRandom

Generates txt files with simulated preamplifier (charge sensitive amplifier) from a scintilator / pmt tube. 
Use for testing and tuning of the pulse shaping filter...
"""
import random
import matplotlib.pyplot as plt
import numpy

file = open("simulatedData.txt", "w")


#User Parameters
data = []
v = 0
samples = 10000
noise = True
noiseFactor = 0.02
decayFactor = 0.002

#Main Numeric loop
event = 0
for i in range(samples):
    #Decide if event happend
    if(random.randint(0,1000) > 999):
        event = 25
        eventAmpStep = random.randint(1, 1000)/(1000*25)
    if(event > 0):
        v += eventAmpStep
        event -= 1
    #Simulate saturation
    if(v > 5):
        v = 5   
    #Simulate exp. decay
    v -= v*decayFactor
    #Catch negative voltage (preamplifier forced to ground)
    if(v < 0):
        v = 0
    data.append(v)       
    
#Add withe noise    
if(noise == True):
    data += numpy.random.normal(0, noiseFactor, size=samples)
  
#Write to file, plot etc.
for i in range(samples):
    file.write(str(data[i]) + "\n")
    
file.close()    
plt.plot(data)
