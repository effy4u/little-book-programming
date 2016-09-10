'''
Aim:	Write a program to work out the areas of a rectangle.
		Collect the width and height of the rectangle from the keyboard
		Calculate the area and display the result.
            
Author:	David James
Date:	2016-06-17
'''

# Ask the user for the length and width of the rectangle
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))

# Calculate the area of the rectangle
area = length * width

# Display the dimensions and area of the rectangle
print("The area of a rectangle with dimensions {} by {} is {}".format(length, width, area))