# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:33:22 2023

@author: Torin
"""
import random
import hashlib

'''
function portion of code
'''
def generate_file(files, g_or_e): #takes filename and whether it is good or evil and generates a text file with 10 places where the value can differ.
    with open(files, 'w') as file:
        pizzaaddress = random.randint(1,100)
        fazbears = random.choice(['Freddy', 'Bonnie', 'Chica', 'Foxy'])
        fazbears2 = random.choice(['Freddy', 'Bonnie', 'Chica', 'Foxy'])
        while fazbears == fazbears2:
            fazbears2 = random.choice(['Freddy', 'Bonnie', 'Chica', 'Foxy'])
        puncchoice = random.choice(['!', '.'])
        maybecolonmaybecomma = random.choice([':', ','])
        maybespace = random.choice([" ", ""])
        if g_or_e == 'G':
            file.write(f"This document contracts the bearer to work the night shift at the address listed below:\n")
            file.write(f"Name: Mike Schmidt\n")
            file.write(f"Employer: Freddy's Pizza\n")
            file.write(f"Address: 230{pizzaaddress} Beary Lane, Pasadena, CA.\n")
            file.write(f"The bearer must work for 5{maybespace} nights from 12am-{maybespace}6am and will earn $80 per night.\n")
            file.write(f"Various animatronics such as {fazbears} & {fazbears2} might come to life, but it's no big deal{puncchoice}\n")
            file.write(f"In particular{maybecolonmaybecomma} look out for Golden Freddy.{maybespace}\n")
            file.write(f"The bearer may not leave before finishing the 5 nights.{maybespace}\n")
            file.write(f"Upon completion of the 5 nights, the bearer will be granted release of this contract and leave Freddy's Pizza{puncchoice}\n")
        else:
            file.write(f"This document contracts the bearer to work the night shift at the address listed below:\n")
            file.write(f"Name: Mike Schmidt\n")
            file.write(f"Employer: Freddy's Pizza\n")
            file.write(f"Address: 230{pizzaaddress} Beary Lane, Pasadena, CA.\n")
            file.write(f"The bearer must work for 5{maybespace} nights from 12am-{maybespace}6am and will earn $30 per night.\n")
            file.write(f"Various animatronics such as {fazbears} & {fazbears2} might come to life, but it's no big deal{puncchoice}\n")
            file.write(f"In particular{maybecolonmaybecomma} look out for Golden Freddy.{maybespace}\n")
            file.write(f"The bearer may not leave before finishing the 5 nights.{maybespace}\n")
            file.write(f"Upon completion of the 5 nights, the bearer will be stuffed into an animatronic suit and become a new attraction at Freddy's Pizza{puncchoice}\n")
        file.close()

def hashit(files): #hashes file and returns the value of the hash in hex
    with open(files, 'rb') as filetohash:
        hexhash = hashlib.md5(filetohash.read()).hexdigest()
        return hexhash

def collision(goodhashes, evilhashes):
    goodhashindex = -1
    evilhashindex = -1
    goodindex = 0
    while goodindex < len(goodhashes):
        evilindex = 0
        while evilindex < len(evilhashes):
            if str(goodhashes[goodindex])[-5:] == str(evilhashes[evilindex])[-5:]: #takes last 5 characters from each hash and checks for equality
                goodhashindex = goodindex
                evilhashindex = evilindex
                return goodhashindex, evilhashindex  # if collision, return indices
            evilindex += 1 # if no collision, iterate evilindex by 1 and recheck
        goodindex += 1
    return -1, -1 #if never a collision, return -1

'''
"main" portion of code
'''

good_file_collection = ['goodfile{}.txt'.format(i) for i in range(1000)] #generate 1000 good and evil files in the format goodfile(number).txt and evilfile(number.txt). Saves them in 2 lists.
evil_file_collection = ['evilfile{}.txt'.format(i) for i in range(1000)]

goodhashes = [] # lists to hold all hashes
evilhashes = []

for goodfile in good_file_collection: #for every good file, generate its contents, hash it, and save it in the goodhashes list
    generate_file(goodfile, 'G')
    thehash = hashit(goodfile)
    goodhashes.append(thehash)
for evilfile in evil_file_collection: #ditto for the evil files
    generate_file(evilfile, 'E')
    thehash = hashit(evilfile)
    evilhashes.append(thehash)

goodindex, evilindex = collision(goodhashes, evilhashes) #call collision function to collect indexes of similar documents

if (goodindex != -1) and (evilindex != -1): # if collision doesn't return -1, prints out the full hash of the collided docs. Otherwise, prints out no collision
    print(f'Match found between {good_file_collection[goodindex]} and {evil_file_collection[evilindex]}\n')
    print(f"Full hash of good doc: {goodhashes[goodindex]}\n")
    print(f"Full hash of evil doc: {evilhashes[evilindex]}\n")
else:
    print('No matches found.\n')
