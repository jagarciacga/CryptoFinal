# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:35:06 2023

@author: Torin Kearney
Collaborated with Kyle Boe on general ideas and utilized online resources such as GeeksforGeeks and W3Schools for clarifying errors and finding fixes to issues.
"""
#Per the assignment, the minimum possible Vigenere key length is 9, and the maximum possible is 16. This code is written with that in mind.

def shiftedArrays(arraytoshift):
    allshiftedarrays = [] # Creates allshiftedarrays, which will hold all the arrays shifted by 9-16 spaces
    min = 9
    max = 17 # min of 9 and max of 17 will create 8 arrays, each will be shifted from 9-16 places

    for i in range(min,max):
        shiftedarray = [0] * len(arraytoshift)  # Creates array with all 0s for padding
        for j in range(len(arraytoshift)):
            if j >= i:
                shiftedarray[j] = arraytoshift[j - i] # replaces 0s in shiftedarray with corresponding letters in arraytoshift. For example, with an i (proposed key length) of 10, the loop will set the 10 index of shifted array to the 0 index of arraytoshift. The loop will then set the 11 index of shifted array to the 1 index of arraytoshift, and so on
        allshiftedarrays.append(shiftedarray) # appends the shifted array to allshiftedarrays. At the conclusion of the entire loop, allshiftedarrays will contain 8 separate arrays, shifted right from 9-16 places
    return allshiftedarrays #returns allshiftedarrays

def findMatches(theshiftedarrays, thenonshiftedarray):
    iterations = 0 # initializes variables and an array that will hold the number of matches for each proposed key length
    matchesvalues = []
    samevalues = 0
    while iterations < 8: # will run through the loop 8 times, same number as the arrays in theshiftedarrays
        for x in range(len(thenonshiftedarray)):
            if (theshiftedarrays[iterations][x] == thenonshiftedarray[x]): # checks to see if each value in theshiftedarrays corresponds with the value in the same index in thenonshiftedarray. If so, adds 1 to the count of matching values.
                samevalues = samevalues + 1
        matchesvalues.append(samevalues) # appends the number of matching values to matchesvalues
        iterations = iterations + 1 
        samevalues = 0 #resets count of matching values for the next proposed key length
    return matchesvalues

def findKeyLength(arrayofmatches):
    maxvalue = arrayofmatches.index(max(arrayofmatches)) # Gets the index of the maximum value in the arrayofmatches
    return maxvalue + 9
    
def splitLines(keyLength, originalarray):
    bins = [] # initializes list to hold all of the "bins" of letters
    for i in range(keyLength):
        bin = []
        for letter in range(i, len(originalarray), keyLength): # runs the loop starting at position i in the original array of letters, appends the letter to bin, and increments i by the key length, before then appending the value in the new index i to bin, and so on
            bin.append(originalarray[letter])
        bins.append(bin) # adds bin of letters to the collection of bins
    return bins

def writetoFile(binsofletters):
    for i, bin in enumerate(bins): # for a number i and all letterbins in bins, create a newfile named output<number>.txt, open it for writing, and write the bin to that file, before printing out the file creation statement
       with open(f"output{i}.txt", "w") as letterbins: 
           for letter in bin:
               letterbins.write(f"{letter}")
           print(f"Created output{i}.txt")

#EDIT FILNAME IN BELOW COMMAND
file = open("ciphertext.txt","r")
#EDIT FILENAME IN ABOVE COMMAND

data = file.read() # Reads the file, initalizes a list, and appends each character in the text to the list
characterlist = []
for letter in data:
    characterlist.append(letter)

print("To change the file, open this script in the IDE of your choice and edit the open function on line 57.\n")
result = shiftedArrays(characterlist) # calls the shiftedArrays function with the list of characters and stores the resulting list in result
indexes = findMatches(result, characterlist) # calls the findMatches function with the shifted arrays and the original array of characters, and stores the resulting list of matches in indexes
actualkeyLength = findKeyLength(indexes) # calls the findKeyLength function with the list of matches and stores the resulting key length in actualkeyLength
print(f"The estimated key length is {actualkeyLength}.")
bins = splitLines(actualkeyLength, characterlist) # calls the splitLines function and stores the resulting bins of letters in bins
writetoFile(bins) # calls writetoFile with the letter bins and writes the letters to their own separate files
file.close() # closes file