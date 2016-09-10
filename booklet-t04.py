'''
Aim:	Write a program that will work out the
		distance travelled if the user enters in the
		speed and the time.
            
Author:	David James
Date:	2016-06-17
'''

# Ask the user for the speed and time
speed = float(input("What was the speed of your journey in miles per hour? "))
time = float(input("What was the time of the journey in hours? "))

# Calculate the area of the rectangle
distance = speed * time

# Display the speed, time and distance travelled
print("The distance travelled when travelling at {} mph for {} hours is {} miles.".format(speed, time, distance))