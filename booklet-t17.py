print(
'''-------------------------------------------------------------------------------------------------------------------
Aim: Convert a UMS score into a grade. The function will return 'A' -> 'U'.
         The function needs the parameter - mark.
         'A' >= 80%; 'B' >= 70%; 'C' >= 60%; 'D' >= 50%; 'E' >= 40%; 'U' for less than 40%
         Maximum mark is 80, and there are three modules to enter marks for.
Author: David James
Date: 2016-07-01
------------------------------------------------------------------------------------------------------------------'''
)
def umsScore(mark) :
    percent = mark/80*100
    if percent >= 80 :
        grade = 'A'
    elif percent >= 70 :
        grade = 'B'
    elif percent >= 60 :
        grade = 'C'
    elif percent >= 50 :
        grade = 'D'
    elif percent >= 40 :
        grade = 'E'
    else :
        grade = 'U'
    return grade

mod1Mark = int(input("Enter module 1 mark: "))
mod2Mark = int(input("Enter module 2 mark: "))
mod3Mark = int(input("Enter module 3 mark: "))
meanMark = (mod1Mark + mod2Mark + mod3Mark)/3

print('''
Results
----------
Module 1: {}
Module 2: {}
Module 3: {}
Overall : {}
'''.format(umsScore(mod1Mark), umsScore(mod1Mark), umsScore(mod3Mark), umsScore(meanMark)))

