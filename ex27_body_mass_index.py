# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 27
# Date: 26.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 27: Body Mass Index

print "Enter your weight in kilograms:"
w = float(raw_input("> "))

print "Enter your height in meters:"
h = float(raw_input("> "))

print "Your body mass index is:", round(w / (h * h), 2)