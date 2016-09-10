print('''
Aim
===
A procedure to draw spaces and stars.
The parameters are the number of spaces and the number of stars.

Author: David James
Date: 2016-07-01
''')

def drawStars(spaces, stars) :
    for count in range(0, spaces) :
        print(" ", end="")
    for count in range(0, stars) :
        print("*", end = "")

drawStars(3, 3)
print()
drawStars(3, 3)
print()
drawStars(4, 1)
print()
drawStars(3, 3)
print()
drawStars(0, 7)
print()
drawStars(3, 3)
print()
drawStars(3, 1)
drawStars(1, 1)
print()
drawStars(1, 2)
drawStars(1, 2)
