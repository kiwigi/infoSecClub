#This program, given a hash and a password dictionary will find a password
#It hashes every password in the dictionary and compares it to the given hash
#If the hashed word from the dictionary and the hash inputted match, then it means that
#The word is the hash before it was hashed AKA a password. 

import hashlib

#input hash
hashedPss = input("Enter md5 hash: ")
#input name of file that contains a list of passwords
listOfPasswords = input("File name: ")
#bool that reflects wether password is found or not
isFound = 0

try:
    pass_file = open (listOfPasswords, "r")
except:
    print("that file cannot be found. ")
    quit()

for word in pass_file:

    encoded = word.encode('utf-8')
    #hex obj must be 'digested', whatever that means
    digest = hashlib.md5(encoded.strip()).hexdigest()

    if digest == hashedPss:
        print("password found.")
        print("it is "+ word)
        isFound = 1
        break
if isFound == 0:
    print("Could not find any passwords in the list that match that hash.")