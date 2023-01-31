# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 21:20:50 2022

@author: osjac
"""

import numpy as np
import csv

"""
This py script contains the functions needed to create the legal positions mask,
it contains functions for each room tile seen below. Each part is 4m x 4m. 
    => This can be adjested but must change vaule in room var definition.
    => New tile types could also be added
Access the corrisponding cvs file to create your own room layout, using
bh, th, lh, rh, e and f to denote which tiles to use. See githubAddess for 
diagram showing process.
"""

def BH():
    """
    Bottom Half Tile (4 x 4), ID: bh
    """
    return np.array([[True ,True ,True ,True ],
                     [True ,True ,True ,True ],  
                     [False,False,False,False],  # ░░░░
                     [False,False,False,False]]) # ████

def LH():
    """
    Left Half Tile (4 x 4), ID: lh
    """
    return np.array([[False,False,True ,True ],
                     [False,False,True ,True ],
                     [False,False,True ,True ],  # ██░░
                     [False,False,True ,True ]]) # ██░░

def RH():
    """
    Right Half Tile (4 x 4), ID: rh
    """
    return np.array([[True ,True ,False,False],
                     [True ,True ,False,False],
                     [True ,True ,False,False],  # ░░██
                     [True ,True ,False,False]]) # ░░██

def TH():
    """
    Empty Tile (4 x 4), ID: th
    """
    return np.array([[False,False,False,False],
                     [False,False,False,False],
                     [True ,True ,True ,True ],  #████
                     [True ,True ,True ,True ]]) #░░░░

def E():
    """
    Bottom Half Tile (4 x 4), ID: e
    """
    return np.array([[True ,True ,True ,True ],
                     [True ,True ,True ,True ],
                     [True ,True ,True ,True ],  #░░░░
                     [True ,True ,True ,True ]]) #░░░░

def F():
    """
    Full Tile (4 x 4), ID: f
    """
    return np.array([[False,False,False,False],
                     [False,False,False,False],
                     [False,False,False,False],  #████
                     [False,False,False,False]]) #████

def LC():
    """
    Left collum tile (4 x 4), ID: lc
    """
    return np.array([[False,True ,False,True ],
                     [False,True ,False,True ],
                     [False,True ,False,True ],  #█░█░
                     [False,True ,False,True ]]) #█░█░


def generateMask():
    """
    Funtion that creates the mask of legal move locations, reads a cvs file to
    do this. Also finds the width and hight of the room (also defined in the cvs
    file). 

    Returns
    -------
    mask :  2D numpy array of booleans
        Mask of illegal square meters.
    ROOM : 2D List of floats
        2D array defining the size of the room.

    """
    file = open("moreristricedRoom.csv") #open file containing room plan
    reader = csv.reader(file, delimiter=',') #create reader
    temp2 = []
    w = 0
    h = 0
    #read each line and coloum and create the 2d numpy array
    for row in reader:
        h = h + 1 #keep track of hight
        temp = []
        for column in row:
            w = w + 1 
            if column == "bh":
                temp.append(BH())
            elif column == "th":
                temp.append(TH())
            elif column == "lh":
                temp.append(LH())
            elif column == "rh":
                temp.append(RH())
            elif column == "e":
                temp.append(E())
            elif column == "lc":
                temp.append(LC())
            elif column == "f" or "ï»¿f": #not sure where this comes from but is
                temp.append(F())          #present at the start of the cvs file

        temp1 = np.hstack(temp)
        temp2.append(temp1)

    mask = np.vstack(temp2) 
    w = int(w/h) #find width
    file.close() #close reader
    ROOM = [[0,h*4],[0,w*4]]
    
    return mask, ROOM     









