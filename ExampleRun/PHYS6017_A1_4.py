# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:42:17 2022

@author: osjac
"""

from CovidRandWalkSim import covidrwsim
from RoomGen import generateMask
from scipy.optimize import curve_fit
import numpy as np
from alive_progress import alive_bar
import pandas as pd
import time
import matplotlib.pyplot as plt

df1 =  pd.DataFrame()

plotNum = 1

MASK, ROOM = generateMask()

SIMNUM = 100

collect = {}

N = 50
S = 1343
A = -0.05
im = 0
MP = [0.99,0.999,0.9999]
MT = 0
num = 1

with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(0,SIMNUM):
        numberInf = 0
        temp = covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1]
        subCollect = []
        for o in range(0,S):    
            numberInf = numberInf + temp.count(o)
            numberNotInf = N - numberInf
            subCollect.append(numberInf)
            
        collect["RUN"+str(i)] = subCollect
        bar()

df = pd.DataFrame(collect)
df1['mean1'] = df.mean(axis=1)      


collect = {}

N = 50
S = 1343
A = -0.05
im = 0
MP = [0.01,0.999,0.9999]
MT = 0
num = 1

with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(0,SIMNUM):
        numberInf = 0
        temp = covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1]
        subCollect = []
        for o in range(0,S):    
            numberInf = numberInf + temp.count(o)
            numberNotInf = N - numberInf
            subCollect.append(numberInf)
            
        collect["RUN"+str(i)] = subCollect
        bar()

df = pd.DataFrame(collect)
df1['mean2'] = df.mean(axis=1)     

collect = {}

N = 50
S = 1343
A = -0.05
im = 0
MP = [0.001,0.01,0.9999]
MT = 0
num = 1

with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(0,SIMNUM):
        numberInf = 0
        temp = covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1]
        subCollect = []
        for o in range(0,S):    
            numberInf = numberInf + temp.count(o)
            numberNotInf = N - numberInf
            subCollect.append(numberInf)
            
        collect["RUN"+str(i)] = subCollect
        bar()

df = pd.DataFrame(collect)
df1['mean3'] = df.mean(axis=1)     

collect = {}

N = 50
S = 1343
A = -0.05
im = 0
MP = [0.32,0.82,0.96]
MT = 0
num = 1

with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(0,SIMNUM):
        numberInf = 0
        temp = covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1]
        subCollect = []
        for o in range(0,S):    
            numberInf = numberInf + temp.count(o)
            numberNotInf = N - numberInf
            subCollect.append(numberInf)
            
        collect["RUN"+str(i)] = subCollect
        bar()

df = pd.DataFrame(collect)
df1['mean4'] = df.mean(axis=1)     


df1.to_csv(str(SIMNUM)+"_simulations_comparing_mask_types_1.csv")