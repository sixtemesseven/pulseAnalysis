# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:51:16 2019

@author: justRandom

Test of a Pulse Shaper and Pulse Hight Detector based on post processing of digitized preamp / charge sensitive amplifier data.

The filter is modeled after the "Trapezoidal Filter" described in: https://www.science.mcmaster.ca/radgrad/images/6R06CourseResources/4RA34RB3_Lecture_Note_6_Pulse-Processing.pdf
"""


import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal


#Get data
#file = open("simulatedData.txt", "r")
file = open("1msp.txt", "r")
data = []
data = file.read()
data = data.split(',')
for i in range(len(data)):
    data[i] = float(data[i])
file.close()
    
#Filter Parameters
L = 100 #L*1/sampleFrequency correspons to deltaTl
G = 0 #Seperation Gap
lowReject = 0.3 #Zeros everyting below this value
#Filter Calculations
lenghtToFilter = len(data) - L*2 - G*2
fData = []
#Calculate mov average and offset mov average
for i in range(lenghtToFilter):
    sumL1 = 0
    sumL2 = 0
    for j in range(L):
        sumL1 += data[i+j]
        sumL2 += data[L+G+i+j]
    Vav1 = (1/L)*sumL1
    Vav2 = (1/L)*sumL2
    Vout = Vav1-Vav2
    #Get rid of negative overshoot
    if(Vout < lowReject):
        Vout = 0
    fData.append(Vout)



peakPosN = scipy.signal.find_peaks(fData, distance=100)[0]

peakVal = []
peakPos = []
for i in range(len(peakPosN)):
    peakVal.append(fData[peakPosN[i]])
    peakPos.append(int(peakPosN[i]))

'''
#Debug Print filtered with marked peaks    
plt.cla()
plt.plot(fData, markevery=peakPos, marker='x')
plt.plot(data)
'''

bins = 100
low = 0
high = 2
hist = np.histogram(peakVal, bins=bins, range=(low,high))[0]
xAxis = []
Abins = []
every = 20
for i in range(int(bins/every)):
    xAxis.append((high-low)/bins*i*every)
    Abins.append(i*every)


#plt.plot(fData)
print(peakVal)
plt.xticks(Abins, xAxis)
plt.plot(hist)



    
        
        
    



