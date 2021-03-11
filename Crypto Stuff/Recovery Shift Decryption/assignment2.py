# Author: Omer Basar
# Class: CSC-381-001
# Assignment 2: Recover Shift
# Filename: assignment2.py
# Version: 2/7/21
# Additional Note: Christopher Benson helped in the sense that he helped explain
# the directions to me in a more clear way that made it easier to understand

# ----------------------------------------------------------------
# Initialize variables to be used
# This is the cipher to be decrypted and its length
cipherText = "lcllewljazlnnzmvyiylhrmhza"
cipherLength = len(cipherText)


# ----------------------------------------------------------------
'''
frequencyAnalysis: Computes the frequencies of each letter of the given ciphertext and prints out the results
@Parameter: N/A
@Precondition: A ciphertext is provided
@Postcondition: A frequency table is displayed
'''
def frequencyAnalysis():
    # Create a dictionary that stores the alphabet and their frequencies
    alphabetDict = {}
    for i in range(0, 26):
        # Use ASCII codes to call in the appropriate characters
        alphabetDict[chr(97 + i)] = 0

    # Increment each found letter's count by one
    for i in range(0, cipherLength):
        storeChar = cipherText[i]
        alphabetDict[storeChar] += 1

    # Displays a frequency table of all the letters of the alphabet
    for i in range(0, 26):
        print("" + chr(97 + i) + ": " + str(alphabetDict[chr(97 + i)] / cipherLength))

    # After executing this function, the letter with the highest frequency was the letter L
    # A quick internet search reveals that the most common letter in the English alphabet is the letter E
    # If we apply that logic, then performing a 7 letter shift to the left should make the most common
    # letter E and possibly reveal the plaintext
    # Source: https://www.google.com/search?hl=en&q=the%20most%20common%20letter
    # Source: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html


# ----------------------------------------------------------------
'''
decryptionCode: Takes a ciphertext and performs a shift to decrypt the message
@Parameter: N/A
@Precondition: A ciphertext is provided
@Postcondition: Displays the plaintext message
'''
def decryptionCode():
    # Create a list that stores the alphabet
    alphabetList = []
    for i in range(0, 26):

        # Use ASCII codes to call in the appropriate characters
        alphabetList += chr(97 + i)

    # Initialize an empty string that will be used to store the shifted text
    shiftedText = ""

    # Iterate through each index of the ciphertext
    for k in range(0, cipherLength):
        # Determine which index the character from the ciphertext is in the alphabet list
        position = alphabetList.index(cipherText[k])
        # Perform the shift of 7 positions to the left
        position = (position - 7) % 26
        # Add the shifted letter to the string that stores the shifted text
        shiftedText += alphabetList[position]

    # Print the decrypted message
    print("The plaintext was: " + shiftedText)


# ----------------------------------------------------------------
# The frequencyAnalysis function is not called due to the moodle grader not accepting its output
# Call the decryptionCode function
decryptionCode()