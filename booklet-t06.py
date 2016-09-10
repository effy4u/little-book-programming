'''
Aim:
	Make a game for seeing how good people are at guessing when 10 seconds have elapsed.
Steps:
	Tell them to hit enter key when ready
	Get the first time in seconds
	Get them to hit the enter key when they think time has elapsed
	Get the second time in seconds
	Subtract first time from the second time
	Tell them how close to 10 the answer was.
Author:	David James
Date: 	2016-06-19
'''

#imports
import time

#	Start the timer when the user presses enter
input('''
\tPress the enter key to start the timer.
\tWait for 10 seconds and press enter again.
\tThis program will then tell you how good your internal clock is.
''')

# Store the time now
startTime = time.time()

# Calculate the perfect time
perfectTime = time.time() + 10

# Display a message to remind the user to press enter after 10 seconds
input("\tPress enter after 10 seconds...")

# Store the time now
endTime = time.time()

# Calculate the users guess in seconds
usersTime = endTime-startTime

# Display the users guess for 10 seconds
print("\n\tYou guessed {:.2f} seconds.".format(usersTime))

# Display how far from 10 seconds the users guess was
print("\tYour error was {:.2f} seconds.\n".format(10-usersTime))
