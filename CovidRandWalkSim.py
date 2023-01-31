# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:18:53 2022

@author: osjac
"""

import random
import numpy as np
import math
from time import time

#random.seed(0)
#np.random.seed(0)

class human:
    """
    A Class repensenting a Human
    
    Attributes:
        - Azimuth: Direction the person is looking (float)
        - Position: x and y coords (numpy array of floats)
        - Move Mask: Mask of illegal square meters (2D numpy array of booleans)
        - Index: Unique ID for each human (string)
        - Mask Type: Does person have mask on? if so what type? (int, 0,1,2 or 3)
        - Infected: Is this person infected with COVID-19? (boolean)
        - Contagious: Will this Infected person Spread COVID-19? (boolean)
        - Immunity: What is the chance this person will become infected in a contact event (flaot, 0 to 1)
        - Droplet Distance: Distance in which COVID-19 spreads in environment (float)
        - Mask Inefficiency: The base inefficiency of the mask the person is using (float, 0 to 1) 
        - Infect Factor B: Helps define the overall MaskInefficiency that depends on distance (float)
        - Time Infected: Time (in step number) when this person became infected (int) but if not infeced then (string)
    
    """
    
    def __init__(self,a,b,c,d,MASK,im,MP):
        """
        Initialisation of Human Class object, set starting attributes from set
        parameters when starting the simulation or from set distibution, i.e. for 
        mask usage, 80% for example.

        Parameters
        ----------
        a, b, c, d, : Int
            Room bounds.
        MASK : numpy 2D array of booleans
            Legal and ilegal movemant mask, indicates where the person can move.
        im : float
            immunity factor, the chance of becoming infected in a contact event.
        MP : list of floats
            Bounds for distibution of mask usage/type.
            eg. [0.32,0.82,0.96] means 32%, 50%, 14% and 4% 

        Returns
        -------
        None.

        """
        self.azimuth = random.uniform(0,2*math.pi)
        
        #Code to place person in starting point
        #loop intill staring position is legal
        temp = True
        while temp:
            newPosition = np.array([random.uniform(a, b-1),random.uniform(c, d-1)])
            if MASK[int(newPosition[0]),int(newPosition[1])]: #If Position is Legal
                break
        self.position = newPosition #Set Starting Position
        
        self.moveMask = MASK
        self.index = ( "#" + str(int(time()/random.randint(1,1000)) ))
        
        
        #Code to set the mask type depending on the population distubution (MP)
        randNum = random.uniform(0, 1)
        if randNum < MP[0]:
            self.maskType = 0
        elif randNum >= MP[0] and randNum < MP[1]:
            self.maskType = 1
        elif randNum >= MP[1] and randNum < MP[2]:
            self.maskType = 2
        else:
            self.maskType = 3
        
        #People start of not infected or contagious    
        self.infected = False
        self.contagious = False
        
        self.immunity = im
        self.timeInfected = "NA"
        
        #Set the face mask propietys depending on the mask type
        if self.maskType == 1:
            self.dropletDistance = 0.61 #m
            self.maskInefficiency = 0.036 #3.6%
            self.infectFactorB = 2.15
        elif self.maskType == 2:
            self.dropletDistance = 0.15 #m
            self.maskInefficiency = 0.0067 #0.67%
            self.infectFactorB = 35.55
        elif self.maskType == 3:
            self.dropletDistance = 0 #m
            self.maskInefficiency = 0.0 #0%
        else:
            self.dropletDistance = 1.25
            self.maskInefficiency = 1.0 #100%
            
    def startInfected(self,MT):
        """
        This funtion is called when a Human Object is set to be starting off 
        as infected and contagious, it will also set the correct face mask
        parameters as well
        """
        self.infected = True
        self.contagious = True
        self.maskType = MT
        
        if MT == 1:
            self.dropletDistance = 0.61 #m
            self.maskInefficiency = 0.036 #3.6%
            self.infectFactorB = 2.15
        elif MT == 2:
            self.dropletDistance = 0.15 #m
            self.maskInefficiency = 0.0067 #0.67%
            self.infectFactorB = 35.55
        elif MT == 3:
            self.dropletDistance = 0 #m
            self.maskInefficiency = 0.0 #0%
        else:
            self.dropletDistance = 1.25
            self.maskInefficiency = 1.0 #100%
        
        
        
    def infectProb(self,distance):
        if (self.maskType == 1) or (self.maskType == 2): 
          return self.infectFactorB*(distance-self.dropletDistance)**2
        else:
            return 0.0
    
    def move(self,amount,a,b,c,d):
        """
        Function of Human Class which changes the position of a Human object

        Parameters
        ----------
        amount : numpy array of floats
            how much to move the person by.
        a, b, c, d, : Int
            Room bounds.

        Returns
        -------
        bool
            Has the move been made?

        """
        newPosition = self.position + amount     
        if self.moveMask[int(newPosition[0]),int(newPosition[1])]: #If Position is Legal
            self.position = newPosition
            return True
        else:
            return False
        
    
    def step(self,a,b,c,d):
        """
        Function of Human Class that moves the person one step, the person will change the 
        direction they are looking randomly sampled from a set normal distubution 
        spanning the average field of view. Then a step amount is made and the person
        is moved in that direction.

        Parameters
        ----------
        a, b, c, d, : Int
            Room bounds.

        Returns
        -------
        None.

        """
        #loop intill new position is legal 
        moved = False
        while not moved:
            self.azimuth = self.azimuth + np.random.normal(scale = .75) #Change direction the person is looking, sample from normal distiution
            #Normalise angle
            if self.azimuth < 0:
                self.azimuth = self.azimuth + math.pi*2 
            elif self.azimuth > 2*math.pi:
                self.azimuth = self.azimuth - math.pi*2 
            
            step = random.uniform(0.8, 1.8) #Step amout 
            add = step * np.array([math.cos(self.azimuth),math.sin(self.azimuth)]) # convert new polar coords to cart
            moved = self.move(add,a,b,c,d) 
        
            
            
            

def findMin(a):
    """
    Custom find minimum function that does not count 0 as the minimum
    The zero is ignored as it coresponds to the person in question when finding 
    the distances to other people.
    """
    temp = 100000000000
    for i in a:
        if (i < temp) and not (i == 0 ):
            temp = i
    return temp


def attraction(person,distances,A,a,b,c,d):
    """
    Function that moves a person towards the closest other person, the amount is 
    defined by an atractiveness factor. If this factor is negaative then they move
    towards the person and if its positive they move away. 
        => Currently this function only moves towards one other person (the closest)
           this is to save computing power but the code can be adjusted to move
           towards every person or the 5 closest people.

    Parameters
    ----------
    person : Human Object
        The person to move.
    distances : Array of floats and Arrays
        Array containing vectors to each other person and their corrisponding magnitudes.
    A : Float
        Atractiveness factor.
    a, b, c, d, : Int
        Room bounds.

    Returns
    -------
    None.

    """
    close = findMin(distances[1]) 
    minIndex = distances[1].index(close)
    attractAmount = (distances[0][minIndex]/distances[1][minIndex])*A #move by factor of unit vector to closest person
    person.move(attractAmount,a,b,c,d)    




def findDistances(person,humanList):
    """
    This function finds the distance from one person to all other people in the 
    human list. The distances are given as difference vectors and there corrisponding
    magnitudes, these are used to find the closest person and to know if they are within
    infection distance.

    Parameters
    ----------
    person : Human Object
        The person to find all the distances from.
    humanList : List of Human Objects
        Main list containing every person in the room.

    Returns
    -------
    humanList : List of Human Objects
        Main list containing every person in the room.
    vectDistances : 2D list containing numpy arrays and floats 
        Holds the distances to all other people in the human list.

    """
    vectDistances = [[],[]]
    for u in humanList: #loop over all people in room, so u and u and u
        diffVec = person.position - u.position  #diffence vectors
        diffVecNorm = np.linalg.norm( diffVec ) #mag of diffence vectors
        vectDistances[0].append(diffVec)
        vectDistances[1].append(diffVecNorm)
        
    return humanList, vectDistances


def nowInfected(human,distances1,humanList,N):
    """
    Function that decides if a person has become infected.

    Parameters
    ----------
    human : Human Object
        Person to test if they are now infected.
    distances1 : 2D list containing numpy arrays and floats
        Holds the distances to all other people in the human list..
    humanList : List of Human Objects
        Main list containing every person in the room.
    N : int
        The number of people in this simulation.

    Returns
    -------
    bool
        Is the person now infected?

    """
    for i in range(0,N):
        
        if (distances1[1][i] <= humanList[i].dropletDistance):
        
            if (humanList[i].contagious) and (random.uniform(10**-6, 1) <= human.maskInefficiency + human.infectProb(distances1[1][i]) ):
                if random.uniform(0, 1) >= human.immunity:
                    return True
    return False




def covidrwsim(N,S,A,ROOM,MASK,im,num,MP,MT):
    """
    Main Simulation function

    Parameters
    ----------
    N : Int
        Number of people to simulate.
    S : Int
        Number of steps to simulate.
    A : float
        Attractiveness Parameter.
    ROOM : 2D list of floats
        Defines the room size. 
    MASK : 2D numpy array of booleans
        Mask of illegal square meters
    im : float
        immunity factor, the chance of becoming infected in a contact event.
    num : int
        Number of people to start infected.    
    MP : list of floats
        Bounds for distibution of mask usage/type.
        eg. [0.32,0.82,0.96] means 32%, 50%, 14% and 4% 
    HM : TYPE
        DESCRIPTION.

    Returns
    -------
    results : List
        List Containing times (in step num, int) of infection for each person,
        length of list is number of infected people after S steps.

    """
    
    #Define the room boundrys
    a = ROOM[0][0]
    b = ROOM[0][1]
    c = ROOM[1][0]
    d = ROOM[1][1]
    
    numContact = 0 #var to hold the number of contact events in this simulation
    
    humanList = [human(a,b,c,d,MASK,im,MP) for _ in range(N)] 
    #loop to start the correct number of starting infected 
    for i in range(0,num):
        humanList[i].startInfected(MT)
    
    #loop for each step    
    for s in range(0,S):
        #loop for each person in simulation every step
        for Human in humanList:
            
            humanList, distances = findDistances(Human,humanList)
            
            if True:#random.randint(0,10) >= 6: #optional stationary period
            
                Human.step(a,b,c,d) #move one step
                attraction(Human,distances,A,a,b,c,d) #move to closest Human
                
                if nowInfected(Human,distances,humanList,N):
                    numContact = numContact + 1
                    if not Human.infected:
                        Human.infected = True
                        Human.timeInfected = s
                    
    #list to hold the results from this simulation
    results = [numContact,[]]
   #results[1].append(0) #optional, inlcude the starting infected in the results
    
   #Record the times in which each person got infected
    for i in humanList:
        if i.infected:
            results[1].append(i.timeInfected)
    return results  
