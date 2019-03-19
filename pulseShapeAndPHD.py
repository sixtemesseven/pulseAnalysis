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
from scipy.stats import binned_statistic

'''
file = open(dataFile, 'r')
data = file.read()
data = data.split(',')
for i in range(len(data)):
    data[i] = float(data[i])
    '''
    
data = [] 
for i in range(1000):
    data.append(0)
for i in range(10000):
    data.append(1)


'''
triangle = []
st = A / F
for i in range(F):
    triangle.append((i+1)*st)
for i in range(T):
    triangle.append(A)
for i in range(F):
    triangle.append(A-(i+1)*st)
    '''

triangle = scipy.signal.triang(1000)

#Convolute with triangle / trap
#fData = scipy.signal.convolve(data, triangle) /sum(triangle)
fData = np.convolve(data, triangle) / sum(triangle)

#Pulse hight via scipy
distance = 0 #Minimum peak seperation 
peakPos = scipy.signal.find_peaks(fData, distance=500)[0]
peakVal = []
for i in range(len(peakPos)):
    peakVal.append(fData[peakPos[i]])

#Bin results
binned = numpy.histogram(peakVal, bins=100, range=(0,10))

#Clear old Plots
plt.cla()
#Data Plots
plt.plot(fData)
plt.plot(data)
plt.plot(triangle)
#plt.plot(binned[0]) #Print Histogram

        
        
    



