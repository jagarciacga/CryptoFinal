 # -*- coding: utf-8 -*-
"""
Torin Kearney
Cryptography PEX 3
Due Date: 18OCT23
"""
import random

def calcKandM(n): #calculates k and m for n-1 = 2^k * m
    k = 0
    m = 0
    nminus1 = n - 1
    while nminus1 % 2 == 0: # while n-1/2 still produces an even number, add 1 to k and redivide n-1 by 2
        k += 1 
        nminus1 = nminus1 // 2
    m = nminus1 # when division finally produces an odd number, m is the number itself
    return k, m

def MillerRabin(n, witnessnumber, k, m):
    if witnessnumber > (n-3): # if number of witnesses requested is too large, print that out and exit the function by returning -1
        print(f"Number of witnesses is too large. The bounds are [2, {n-2}], so max number of witnesses can be {n-3}.")
        return -1
    witnesses = []
    i = 0
    while i < witnessnumber: # selects random witness from allowed bounds, checks to see if it is already in the witness list, and adds it to the list if it isn't.
        witnesscandidate = random.randint(2,n-2)
        if witnesscandidate not in witnesses:
            witnesses.append(witnesscandidate)
            i += 1
    for x in witnesses: # runs for every witness, unless non-primality is discovered
        complete = False
        intermediateiterator = 0
        kminus1 = k - 1
        print("Witness is " + str(x)) # prints out witness
        while complete == False:
            b0 = (x**m) % n # calculates b0 and prints it out
            print(f"b{intermediateiterator} = " + str(b0))
            if b0 == 1 or b0 == (n-1): # if b0 is +-1, prints that n is probably prime and exits the loop
                print(f"b0 is + or - 1 mod {n}, so {n} is probably prime. \n")
                complete = True
            else: # if b0 is not +-1, begins this loop
                intermediateiterator += 1
                b = (b0**2) % n # calculates b1
                while intermediateiterator <= kminus1: # runs k-1 times, unless primality or non-primality is discovered
                    print(f"b{intermediateiterator} = " + str(b)) # prints out b
                    if b == 1: # if b = 1, prints out that n is composite, with a factor of the witness - 1 and returns -1 to break out of the loop and the function
                        print(f"{n} is composite with a factor of " + str((x) - 1))
                        return -1
                    elif b == (n - 1): # if b = -1, prints out that n is probably prime and breaks out of the entire loop
                        print(f"b{intermediateiterator} is -1 mod {n}, so {n} is probably prime.")
                        complete = True
                        break
                    else: # if b does not equal +- 1, then calculate the next b and increase the iterator
                        intermediateiterator += 1
                        b = (b**2) % n
                else: # if b(k-1) does not equal -1, and the loop isn't broken from another b equalling +-1, then it prints out that n fails Fermat and is therefore composite
                    print(f"{n} fails Fermat and is composite.")
                    return -1

n = input("Enter an odd number to test for primality: ") # prompts user to enter a number for n and witnessnumber, checks if it actually is a number, and converts it to an integer if it is
numbercheck = n.isnumeric()
while numbercheck == False:
    n = input("Enter an odd NUMBER to test for primality: ")
    numbercheck = n.isnumeric()
n = int(n)

witnessnumber = input("Enter the number of witnesses desired: ")
witnesscheck = witnessnumber.isnumeric()
while witnesscheck == False:
    witnessnumber = input("Enter the NUMBER of witnesses desired: ")
    witnesscheck = witnessnumber.isnumeric()
witnessnumber = int(witnessnumber)

k,m = calcKandM(n) # calls calcKandM with the requested n, and saves the return values into k and m
MillerRabin(n, witnessnumber, k, m) #calls MillerRabin with n, witnessnumber, and the returned k and m
                        
                        
