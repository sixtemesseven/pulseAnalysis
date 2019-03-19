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
import math
from sympy import *
from numpy import diff

file = open("simulatedData.txt", "w")

#User Parameters
samples = 10000 #lenght of simulated file

noiseFactor = 0.00 #Higher increases noise, set zero to disable
decayFactor = 0.003 #Higher decays quicker
eventProbability = 0.9995 #Lower is more probable
preampSaturation = 5 #Max Value before preamp saturates
randomHight = False #Random pulse Hights 

random.seed(1) #optional add seed to get same values back

#Main Numeric loop
data = []
v = 0
event = 0
for i in range(samples):
    #Decide if event happend
    if(random.randint(0,1000) > (eventProbability*1000)):
        if randomHight == True:
            #events sets stepness of rising flank (linear rise)
            event = 25
            eventAmpStep = random.randint(1, 1000)/(1000*25)
        else:
            event = 2
            eventAmpStep = 0.01
    #If an event is occuring add linear rise
    if(event > 0):
        v += eventAmpStep
        event -= 1
    #Simulate saturation of preamplifier
    if(v > preampSaturation):
        v = preampSaturation   
    #Simulate exp. decay
    v -= v*decayFactor
    #Catch negative voltage (simulated preamplifier us pulled to ground)
    if(v < 0):
        v = 0
    data.append(v)       
    
#Add withe noise    
data += numpy.random.normal(0, noiseFactor, size=samples)

  
#Write to file, plot etc.
comma = ','
for i in range(len(data)):
    if i == len(data)-1:
        comma = ''
    file.write(str(data[i]) + comma)
    
file.close()    
plt.plot(data)
