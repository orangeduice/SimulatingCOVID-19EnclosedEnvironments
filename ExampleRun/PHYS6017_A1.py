# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:32:34 2022

@author: osjac
"""

from CovidRandWalkSim import covidrwsim
from RoomGen import generateMask


from alive_progress import alive_bar

plotNum = 0

MASK, ROOM = generateMask()
#ROOM = generateRoom()

import time
import matplotlib.pyplot as plt
import pandas as pd
SIMNUM = 100

collect = {}

#===============================================
plotNum = plotNum + 1
peen = []
N = 50
S = 1343
A = -0.05
im = 0
MP = [0.99,0.999,0.9999]
MT = 0
num = 1
title0 = ("Simulation with" + " N:" + str(N) +" S:" + str(S) + " A:" + str(A)+" Im:" + str(im)+" MP:" + str(MP)+" HM:" + str(MT)+" num:" + str(num))
print(title0)
subCollect = []
with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(SIMNUM):
        NI = len(covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1])
        subCollect.append(NI)
        bar() 
collect["MP"+str(MP)] = subCollect
#===============================================

#===============================================
plotNum = plotNum + 1
peen1 = []
N = 50
S = 1343
A = -0.05
im = 0
MP = [0.01,0.99,0.999]
MT = 0
num = 1
title1 = ("Simulation with" + " N:" + str(N) +" S:" + str(S) + " A:" + str(A)+" Im:" + str(im)+" MP:" + str(MP)+" HM:" + str(MT)+" num:" + str(num))
print(title1)
subCollect = []
with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(SIMNUM):
        NI = len(covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1])
        subCollect.append(NI)
        bar() 
collect["MP"+str(MP)] = subCollect
#===============================================

#===============================================
plotNum = plotNum + 1
peen2 = []
N = 50
S = 1343
A = -0.05
im = 0
MP = [0.001,0.01,0.999]
MT = 0
num = 1
title2 = ("Simulation with" + " N:" + str(N) +" S:" + str(S) + " A:" + str(A)+" Im:" + str(im)+" MP:" + str(MP)+" HM:" + str(MT)+" num:" + str(num))
print(title2)
subCollect = []
with alive_bar(SIMNUM, bar = "circles",spinner = "classic") as bar:  
    for i in range(SIMNUM):
        NI = len(covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT)[1])
        subCollect.append(NI)
        bar() 
collect["MP"+str(MP)] = subCollect
#===============================================

df = pd.DataFrame(collect)
#df['mean'] = df.mean(axis=1)   
#df['std'] = df.std(axis=1)   
df.to_csv('range_of_outcomes_MP.csv')

# results = covidrwsim(N,S,A,ROOM,MASK)
    
# print(results)

# fig, ax = plt.subplots(plotNum,1,sharex=True)


# ax[0].hist(peen)
# ax[0].set_title(title0)
# ax[0].set_ylabel("No. of instanses")

# ax[1].hist(peen1)
# ax[1].set_title(title1)
# ax[1].set_ylabel("No. of instanses")

# ax[2].hist(peen2)
# ax[2].set_title(title2)
# ax[2].set_ylabel("No. of instanses")

# ax[2].set_xlabel("Number of infected at end of sim")
# ax[2].set_xticks(range(0,21))

# fig.show()
