'''
--------------------------------------------------------------
Aim:		A program to work out if someone is old enough to vote
Author:	David James
Date:		2016-06-19
--------------------------------------------------------------
'''

#	Imports
import datetime
import time

# Constants
year = datetime.timedelta(days=365)
voteAge = 18 * year

#	Get the users date of birth
year = input("\nIn which year were you born? ")
month = input("In which month were you born? ")
date = input("On what date were you born? ")
dateOfBirth = datetime.date(int(year), int(month), int(date))

# Work out the date when user can vote
dateOfVote = datetime.date(int(year)+18, int(month), int(date))

# Get the date today
dateToday = datetime.date.today()

# Check if today is after the date of voting
if dateOfVote <= dateToday :
	print("\nCongratulations, you can vote.\n")
else :
	print("\nI am sorry you are not old enough to vote.\n")
