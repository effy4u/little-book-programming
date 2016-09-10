'''
Aim:		Write a program to work out how many days you have lived for.
				Enter date of birth
				Get today’s date
				Get the difference in days between the two dates
				Display result
				
Author:	David James
Date:		2016-06-19
'''

#imports
import datetime

#	Get the users date of birth
year = int(input("In what year were you born? "))
month = int(input("In what month is your birthday (write as a two-digit number)? "))
date = int(input("What is the date of your birthday? "))

#	Convert to datetime format
birthdate = datetime.date(year, month, date)

#	Get today
today = datetime.date.today()

#	Work out how many days since birthday
daysAlive = (today - birthdate).days

#	Display how many days since birthday
print("You have been alive for {} days.".format(daysAlive))
