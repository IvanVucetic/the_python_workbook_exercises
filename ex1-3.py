# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 1-3
# Date: 23.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com



# Exercise 1: Mailing Address

print """
Ivan Vucetic

ul. Krcunova 4
31000
Uzice
"""
# could've printed line by line



# Exercise 2: Hello

print "Please tell me your name."
name = raw_input("> ")
print "Hello,", name



# Exercise 3: Area of a Room

print "Tell me the length of a room in meters."
length = float(raw_input("> "))
print "Tell me the width of the room in meters."
width= float(raw_input("> "))

print "The area of the room is %s sqare meters." % round(length * width, 2)

