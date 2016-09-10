'''
Objective:
    Write a program that will ask you your name
    It will then display ‘Hello Name’
    where ‘Name’ is the name you have entered.

Author: David James
Date: 2016-06-17
'''

# Ask the user for their name
print("What is your name? ")

# Store the users response in the variable 'name'
name = input()

# Output a message that welcomes them by name
print("Hello {}." .format(name))
