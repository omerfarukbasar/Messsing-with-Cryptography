# Author: Omer Basar
# Class: CSC-381-001
# Assignment 3: Solve Affine Cipher
# Filename: assignment3.py
# Version: 2/7/21
# Additional Note: Kaitlyn Torres helped point out a mistake in my manual calculations
# for determining what the formula should be

'''
When it came to solving the affine cipher, we need the equation y = ax + b mod 26. We know that the first
two letters of plaintext are "if" which is ed and their indexes are 8 and 5. The respective indexes for encrypted text
are 4 and 3. When we plug them into the equations we get 4a + b = 8 mod 26 and 3a + b = 5 mod 26. Subtracting them from
each other and we are left with a = 3 mod 26 which is 3. After plugging in the found a value in to find b we get b = 22.
Now we know that our formula is y = 3x + 22 mod 26, plugging the indexes for i and f yields the indexes for e and d,
which confirms our equation is correct.
'''

# ----------------------------------------------------------------
# Initialize variables to be used
# This is the cipher to be decrypted and its length
cipherText = "edsgickxhuklzveqzvxwkzukcvuh"
cipherLength = len(cipherText)

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
        # Perform the shift using the formula y = 3x + 22 modulo 26
        position = ((3 * position) + 22) % 26
        # Add the shifted letter to the string that stores the shifted text
        shiftedText += alphabetList[position]

    # Print the decrypted message
    print("The plaintext was: " + shiftedText)


# ----------------------------------------------------------------
# Call the decryptionCode function
decryptionCode()
