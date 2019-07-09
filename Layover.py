#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:09:20 2019

@author: damienrigden

This program defines a function which takes as an argument a list of flights with
start and end destination and returns a list of those flights in order from
beginning to end. I am not convinced this is the most efficient solution, but 
it works. This function will reach recursion maximum and fail if a broken list
is supplied.

"""

a = ['BOS', 'JFK']
b = ['JFK', 'ATL']
c = ['ATL', 'IAH']
d = ['IAH', 'LAX']

flights = [b, d, a, c]

def layover(flightlist):
    ordered = []
    leftover = []
    
    if len(flightlist) == 0:
        return ordered
    
    for flight in flightlist:
        if len(ordered) == 0:
            ordered.append(flight)
        
        elif flight[0] == ordered[-1][1]:
            ordered.append(flight)
        
        elif flight[1] == ordered[0][0]:
            ordered = [flight] + ordered
        
        else:
            leftover.append(flight)
    
    if len(leftover) == 0:
        return ordered
    
    else:
        return layover(ordered + leftover)
        
print(layover(flights))