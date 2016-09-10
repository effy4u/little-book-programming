'''
Write a program that will generate a random playing card 
when the return key is pressed.
Rather than generate a random number from 1 to 52. 
Create two random numbers – one for the suit and one for the card.
'''

#imports
import random
import sys

#constants
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
number = ["Ace", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

print("Press 'q' to exit the program... ")
choice = ' '
choice = input('Press "Enter" to get a new random playing card...\n')
while choice != 'q' :
    cardNumber = number[random.randint(0, 12)]
    cardSuit = suit[random.randint(0, 3)]
    print("The card drawn was the \"{} of {}\". " .format(cardNumber, cardSuit))
    choice = input('Press "Enter" to get a new random playing card...\n').lower()
