# Author: Omer Basar
# Class: CSC-381-001
# Assignment 1: Decrypt Shift Cipher
# Filename: assignment1.py
# Version: 2/7/21


# This is the cipher to be decrypted
cipherText = "ycvejqwvhqtdtwvwu"

# Create a list that stores the alphabet
alphabetList = []
for i in range(0, 26):

    # Use ASCII codes to call in the appropriate characters
    alphabetList += chr(97 + i)

# Perform a shift 25 times to go through each possible shift combo
for j in range(1, 26):

    # Initialize an empty string that will be used to store the shifted text
    shiftedText = ""

    # Iterate through each index of the ciphertext
    for k in range(0, 17):
        # Determine which index the character from the ciphertext is in the alphabet list
        position = alphabetList.index(cipherText[k])
        # Perform the shift by j amount, loops back to 0 if exceeds 25
        position = (position + j) % 26
        # Add the shifted letter to the string that stores the shifted text
        shiftedText += alphabetList[position]

    # Print the shifted cipher
    print(str(j) + ":" + shiftedText)

# Print the decrypted message
print("The plaintext was: watchoutforbrutus")