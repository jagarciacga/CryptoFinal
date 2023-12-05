#Cryptography Programming Exercise 1
#By Torin Kearney

# 2 arrays, one with letters to compare the file to, and one to keep track of how many times the letters appear
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
unsorted_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #This array will keep the count of each variable, unsorted, so that 
final_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Opens file and reads it; TO CHANGE FILE, EDIT THE FIRST ARGUMENT IN OPEN() BELOW
file = open('textfile.txt','r')
#TO CHANGE FILE, EDIT THE FIRST ARGUMENT IN OPEN() ABOVE

print("To change file to read, open this script in your IDE of choice and edit the filename on line 11.")

while True:
    character = file.read(1) #Reads 1 character in the file
    if not character: #If there is no character (file has ended), break out of the while loop
        break
    if character.islower() != True: #If the character is not lowercase, convert it to lowercase
        character.lower()
    i = 0
    while i < 26: #Compares the read character to the letters in the array, if there is a match, counter in the count array is appropriately updated
        if character == letters[i]:
            count[i] = count[i] + 1
            unsorted_count[i] = unsorted_count[i] + 1
        i += 1

f = 0
frequencytotal = 0
while f < 26:
    frequencytotal = frequencytotal + count[f] #Calculates number of total characters in the file to assist in finding frequency
    f += 1

count.sort(reverse=True)
letter_number_pairs = list(zip(letters, unsorted_count))
sorted_pairs = sorted(letter_number_pairs, key=lambda x: x[1], reverse=True)

final = 0
while final < 26:
    count_variable = 0
    frequency = count[final]/frequencytotal #Calculates frequency for each character
    a = sorted_pairs[final][0]
    print(str(a) + "  " + str(count[final]) + "  " + str(frequency))
    final += 1
        

    
