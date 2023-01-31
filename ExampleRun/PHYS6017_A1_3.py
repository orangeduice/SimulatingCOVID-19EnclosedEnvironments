# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:18:54 2022

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

plotNum = 1

MASK, ROOM = generateMask()

SIMNUM = 100

N = 50
S = 1343
A = -0.05
im = 0
MP = [0.99,0.999,0.9999]
MT = 0
num = 1

collect = {}



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
df['mean'] = df.mean(axis=1)   
df['std'] = df.std(axis=1)   
df.to_csv(str(SIMNUM)+"_RR1_simulations_with" + "_N" + str(N) +"_S" + str(S) + "_A" + str(A)+"_Im" + str(im)+"_MP" + str(MP)+"_MT" + str(MT)+"_num" + str(num)+'.csv')
        