'''
Aim:		See how long it takes people to type the alphabet.
Author:	David James
Date:		2016-06-19
'''

#	Imports
import time

#	Ask the user to press enter, then start typing the alphabet
#	and finally press enter when they have finished.

print('''
\t          Alphabet typing challenge
\t----------------------------------------------
\t1) Press enter to start the timer
\t2) Then start typing the alphabet
\t3) Finally press enter when you have finished.
''')

# Set the correct answer as a string
correctAlphabet = "abcdefghijklmnopqrstuvwxyz"

#	Wait for "enter"
input()

#	Store the start time
startTime = time.time()

# Store the alphabet from the user
userAlphabet = input()

# Store the end time
endTime = time.time()

# Check the user entered the correct alphabet
if userAlphabet == correctAlphabet :
	print("\n\tYou entered the alphabet correctly.")
	print("\tIt took you {:.2f} seconds to type the alphabet.\n".format(endTime - startTime))
else :
	print("\n\tYou did not enter the alphabet correctly.\n")
