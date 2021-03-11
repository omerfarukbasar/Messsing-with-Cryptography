# Author: Omer Basar
# Class: CSC-381-001
# Assignment 4: Character Encoding
# Filename: assignment4.py
# Version: 2/14/21
# Additional Notes: Received refresher on how to use RegEx from the following websites...
# https://re-thought.com/python-regular-expressions/
# https://pythex.org/

# ----------------------------------------------------------------
# Import regular expressions library to be used later
import re
# ----------------------------------------------------------------
'''
shiftMethod: Takes a ciphertext and performs a shift to decrypt the message
@Parameter: N/A
@Return: shiftedText - text that has been shifted
@Precondition: A ciphertext is provided
@Postcondition: Returns the message in a shifted manner
'''
def shiftMethod(cipherText,cipherLength):
    # Create a list that stores the alphabet
    alphabetList = []
    for i in range(0, 26):
        # Use ASCII codes to call in the appropriate characters
        alphabetList += chr(97 + i)

    # Initialize an empty string that will be used to store the shifted text
    shiftedText = ""

    # Iterate through each index of the ciphertext
    for j in range(0, cipherLength):
        # Determine which index the character from the ciphertext is in the alphabet list
        position = alphabetList.index(cipherText[j])
        # Perform the shift using the formula y = 3x + 22 modulo 26
        position = (position + 4) % 26
        # Add the shifted letter to the string that stores the shifted text
        shiftedText += alphabetList[position]

    # Return updated text
    return shiftedText

# ----------------------------------------------------------------
'''
characterEncoder: Takes a ciphertext and encrypts it using various methods
@Parameter: N/A
@Precondition: A ciphertext is provided
@Postcondition: Displays the encrypted text in the form of hex values
'''
def characterEncoder():
    # Initialize variable to be used
    cipherText = "Hello, World!"

    # Remove all whitespace from text
    cipherText.replace(" ", "")

    # Use RegEx to remove all punctuation from the text
    # First parameter is regex expression which means everything except characters a through z
    # Second parameter is the replacement, in this case it deletes the characters
    # Third parameter is essentially the text provided that goes through the filtering
    cipherText = re.sub("[^a-zA-Z]", "", cipherText)

    # Perform case folding, essentially all lowercase
    cipherText = cipherText.lower()

    # Store length of text to be used later
    cipherLength = len(cipherText)

    # Perform lippsasvph shift
    cipherText = shiftMethod(cipherText, cipherLength)

    # Perform case folding, essentially all uppercase
    cipherText = cipherText.upper()

    # Create two lists holding the hex values, one for even positions and one for odd
    oddList = []
    evenList = []

    # Append each character to its appropriate list based on its index after converting to hex value
    for i in range(0, cipherLength):
        if (i % 2) == 0:
            evenList.append(hex(ord(cipherText[i])))
        else:
            oddList.append(hex(ord(cipherText[i])))

    # Print all the even hex values on one line with spacing
    for j in range(0, len(evenList)):
        print(evenList[j], end=" ")

    # Reset print to go to next line
    print()

    # Print all the odd hex values on one line with spacing
    for k in range(0, len(oddList)):
        print(oddList[k], end=" ")
# ----------------------------------------------------------------
# Call the method to commence encoding
characterEncoder()