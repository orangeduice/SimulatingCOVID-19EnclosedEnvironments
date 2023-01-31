# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:06:30 2022

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


S = 1343
A = -0.05
im = 0
MP = [0.99,0.999,0.9999]
MT = 0
num = 1

collect = {}


N = 50

with alive_bar(11, bar = "circles",spinner = "classic") as bar:  
        for im in [0,0.5,0.75,0.9,0.98]:
            subCollect = []
            for i in range(0,SIMNUM):
                IM = im
                temp = covidrwsim(N,S,A,ROOM,MASK,IM,num,MP,MT)[0]
                subCollect.append(temp)
                
            collect["im"+str(im)] = subCollect
            
            
            bar()
            
            
df = pd.DataFrame(collect)
#df['mean'] = df.mean(axis=1)   
#df['std'] = df.std(axis=1)   
df.to_csv('diffNcontactNumsIM.csv')