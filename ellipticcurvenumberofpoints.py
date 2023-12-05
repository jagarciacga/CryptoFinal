# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:09:16 2023

@author: Torin
"""

y = []
x = []

calculatedysquared = []
calculatedx = []
pointsnum = 1

def calcY(yval, ysquared, n):
    for y in range(n):
        yval.append(y)
        val = (y**2) % n
        ysquared.append(val)
    return yval, ysquared

def calcX(xval, xcalcd, b, c, n):
    for x in range(n):
        xval.append(x)
        val = (x**3 + b*x + c) % n
        xcalcd.append(val)
    return xval, xcalcd

def compare(x, y, xcalcd, ysquared, pointsnum):
    for xindex, x2 in enumerate(xcalcd):
        for yindex, y2 in enumerate(ysquared):
            if x2 == y2:
                print(f"Match found between x:{x[xindex]} and y:{y[yindex]}")
                pointsnum += 1
    print(f"Number of points on the elliptic curve: {pointsnum}")
    
# EDIT B, C, AND N BASED ON THE PROBLEM X^3 + BX + C mod N
b = 1
c = 5
n = 17
# EDIT B, C, AND N BASED ON THE PROBLEM X^3 + BX + C mod N

calcY(y, calculatedysquared, n)
calcX(x, calculatedx, b, c, n)
compare(x, y, calculatedx, calculatedysquared, pointsnum)
