# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:50:49 2022

@author: osjac
"""

from CovidRandWalkSim import covidrwsim
from RoomGen import generateMask
from scipy.optimize import curve_fit
import numpy as np
from alive_progress import alive_bar

plotNum = 1

MASK, ROOM = generateMask()
#ROOM = generateRoom()

import time
import matplotlib.pyplot as plt


def fit_function(x,alpha,beta):
    return np.power(x,alpha)*beta



SIMNUM = 100

N = 30
S = 1000
A = -0.05
im = 0
MP = [0.32]
HM = False
num = 1

results1 = []
results2 = []
results3 = []

# for i in range(SIMNUM):
#     results.extend(covidrwsim(N,S,A,ROOM,MASK,im,num,MP,HM)[1])
    
# x_data = range(0,S)
# y_data = []

# for i in range(0,S):
#     y_data.append(results.count(i))


with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(SIMNUM):
        results0 = covidrwsim(N,S,A,ROOM,MASK,im,num,MP,HM)[1]
        #results0.append(0)
        numberInf = 0
        for i in range(0,S):
             
            numberInf = numberInf + results0.count(i)
            numberNotInf = N - numberInf 
            #print(numberNotInf)
            for o in range(0,numberInf):
                results2.append(i)
                #results3.append()
            
            
            for o in range(0,numberNotInf):
                results1.append(i)
                
            
        bar() 
    
popt, pcov = curve_fit(fit_function, xdata=x_data, ydata=y_data, p0=[0.5, 0.1])
print(popt)

xspace = np.linspace(0, 6, 100000)

plt.bar(x_data, y_data)
plt.plot(xspace, fit_function(xspace, *popt))

plt.show()
