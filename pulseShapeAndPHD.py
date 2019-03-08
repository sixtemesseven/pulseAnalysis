# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:51:16 2019

@author: justRandom

Test of a Pulse Shaper and Pulse Hight Detector based on post processing of digitized preamp / charge sensitive amplifier data.

The filter is modeled after the "Trapezoidal Filter" described in: https://www.science.mcmaster.ca/radgrad/images/6R06CourseResources/4RA34RB3_Lecture_Note_6_Pulse-Processing.pdf
"""


import random
import matplotlib.pyplot as plt
import numpy
import scipy.signal


#Get data
file = open("simulatedData.txt", "r")
data = []
for lines in file:
    data.append(float(file.readline()))
plt.plot(data)
file.close()
    
#Filter Parameters
L = 50 #L*1/sampleFrequency correspons to deltaTl
G = 50 #Seperation Gap
lowReject = 0.1 #Zeros everyting below this value
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
    Vout = Vav2-Vav1
    #Get rid of negative overshoot
    if(Vout < lowReject):
        Vout = 0
    fData.append(Vout)

'''
#Pulse Hight detection via local Maxima
peaksPos = scipy.signal.find_peaks(fData)
peaksPos = numpy.ndarray.tolist(peaksPos[0])
plt.plot(fData, '-gD', markevery=peaksPos)
'''

#Pulse High detection via if loops
isRising = False
isFalling = True
peakPos = []
peakVal = []
for k in range(len(fData)-1):
    #Peak
    if(fData[k]>fData[k+1] and isRising==True and isFalling==False):
        peakPos.append(k)
        peakVal.append(fData[k])
        isRising == False
        isFalling == True
    #Has fallen to 0, expect new peak
    if(fData[k] == 0):
        isFalling = False
    #Value rises again, expect new peak
    if(fData[k]<fData[k+1] and isFalling==False):
        isRising = True    
        
print(peakPos)
plt.plot(fData)
        
    
        
        
    



