'''
Aim: Make a game of rock, paper scissors against the computer.
Author: David James
Date: 2016-06-23
'''

# imports
from random import randint

# constants
rock = 1
paper = 2
scissors = 3

# get the users choice of rock, paper or scissors
userChoice = int(input('''
Rock, Paper, Scissors Game
======================
  Make your choice:
  1 - Rock
  2 - Paper
  3 - Scissors
'''))

# get the computer generated value
computerChoice = randint(1, 3)

if userChoice == computerChoice :
    print("The computer chose the same as you so it is a draw\n")
elif userChoice == rock :
    if computerChoice == paper :
        print("The computer chose paper so you lose\n")
    else :
        print("The computer chose scissors so you win\n")
elif userChoice == paper :
    if computerChoice == scissors :
        print("The computer chose scissors so you lose\n")
    else :
        print("The computer chose rock so you win\n")
elif userChoice == scissors :
    if computerChoice == rock :
        print("The computer chose rock so you lose\n")
    else :
        print("The computer chose paper so y1ou win\n")
else :
    print("Error incorrect input!")

