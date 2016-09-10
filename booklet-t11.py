'''
Aim:		Create a program to output the correct responses to logic gates
				OR, AND, XOR, NAND and NOR

Author:	David James
Date:		2016-06-23
-----------------------------------------------------------------------
'''

def orGate(inOne, inTwo):
	if inOne == 1 or inTwo == 1:
		return 1
	else:
		return 0

def andGate(inOne, inTwo):
	if inOne == 1 and inTwo == 1:
		return 1
	else:
		return 0

def xorGate(inOne, inTwo):
	if inOne == inTwo:
		return 0
	else:
		return 1

def nandGate(inOne, inTwo):
	if inOne == 1 and inTwo == 1:
		return 0
	else:
		return 1

def norGate(inOne, inTwo):
	if inOne == 0 and inTwo == 0:
		return 1
	else:
		return 0

#	Get inputs for the gates
input1 = int(input("Enter an input (0 or 1): "))
input2 = int(input("Enter an input (0 or 1): "))

print("{} OR {} outputs {}".format(input1, input2, orGate(input1,input2)))
print("{} AND {} outputs {}".format(input1, input2, andGate(input1,input2)))
print("{} XOR {} outputs {}".format(input1, input2, xorGate(input1,input2)))
print("{} NAND {} outputs {}".format(input1, input2, nandGate(input1,input2)))
print("{} NOR {} outputs {}".format(input1, input2, norGate(input1,input2)))
