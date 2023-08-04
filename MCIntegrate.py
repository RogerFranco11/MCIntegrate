# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:28:51 2023

@author: rjfch
"""

def MCintegrate(f, a, b, n):
    """
    
    Parameters
    ----------
    f : TYPE function
        f returns a float between a and b
    a : TYPE float
        DESCRIPTION. lower limit
    b : TYPE float
        DESCRIPTION. upper limit
    n : TYPE int
        DESCRIPTION, number of random points to take in the box
    Returns
    -------
    integral of f from a to b
    
    """
    from random import random
    from numpy import linspace
    # random returns a random number betwee 0 and 1
    
    x = linspace(a,b, num=n, endpoint=True)
    maxF = max(f(x))
    
    area = 0
    for i in range(n):
        
        #generate a random point in the boxc
        #x between a and b
        #z between 0 and maxF
        randNoX = random()*(b-a)+(b-a)/2
        randNoY = random()*maxF
        if randNoY <= f(randNoX): area += 1
        
    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    return(integral)

if __name__ == "__main__":
    
    #import numpy as np
    #import matplotlib.pyplot as plt

    def f(x) :
        return x**2

    area = MCintegrate(f, 1.,3., 50)
    
    print(area)
