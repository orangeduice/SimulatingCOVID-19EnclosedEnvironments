# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:53:47 2022

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

SIMNUM = 10

N = 30
S = 1000
A = -0.05
im = 0
MP = 0
HM = False
num = 1




# with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
#     for i in range(SIMNUM):
#         results.append(covidrwsim(N,S,A,ROOM,MASK,im,num))
#         bar() 


# results0 = covidrwsim(N,S,A,ROOM,MASK,im,num)
# results0.append(0)
# print(results0)
results2 = []
results1 = []
numberInf = 0

def fit_function(x,A,B):
    return np.power(x,A)*B

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
            
            
            for o in range(0,numberNotInf):
                results1.append(i)
        bar() 
    


popt, pcov = curve_fit(fit_function, xdata=range(0,1000,1), ydata=results2, p0=[0.5, 0.1])

print(popt)

xspace = np.linspace(0, 6, 100000)
    
# results.sort()
# print(results)
# #results = np.transpose(results)
# #for i in range(0,1000):
    
# print(results.count(999))
fig, ax = plt.subplots(plotNum,1,sharex=True)

results = [results2,results1]
#results = [results1,results2]


ax.hist(results, S, density=True, histtype='bar', stacked=True)

plt.plot(xspace, fit_function(xspace, *popt))


#print(results)#np.random.randn(1000, 3))

plt.show()