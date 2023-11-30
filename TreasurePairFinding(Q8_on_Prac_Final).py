# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:24:49 2023

@author: Torin
"""

import math

def findTreasurePair(fac1,fac2,n):
    x = fac1**2 % n
    y = fac2**2 % n # calculate factors^2 mod n
    if x != y: # if x^2 != y^2 mod n, then no treasure pair
        print(f"No treasure pair for {fac1} and {fac2} mod {n}, {fac1}^2 mod {n} is not equal to {fac2}^2 mod {n}")
    else:
        if (fac1 - n) == fac2 or (fac1 - n) == (fac2 * -1): # if x = + or - y mod n, then no treasure pair
            print(f"No treasure pair for {fac1} and {fac2} mod {n}, {fac1} = + or - {fac2} mod {n}")
        elif (fac2 - n) == fac1 or (fac2 - n) == (fac1 * -1):
            print(f"No treasure pair for {fac1} and {fac2} mod {n}, {fac1} = + or - {fac2} mod {n}")
        else:
            print(math.gcd(fac1-fac2,n)) # if treasure pair exists, find factor using gcd(x-y,n)

factor1 = int(input("Enter first (lower) factor: "))
factor2 = int(input("Enter second (higher) factor: "))
mod = int(input("Enter modulus: "))

findTreasurePair(factor1,factor2,mod)

"""
Alternatively, you can delete lines 21-23 and hardcode factors and mods for line 25
"""
