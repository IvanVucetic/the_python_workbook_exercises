# Ben Stephenson - The Python Workbook
#
# Exercise no. 141
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 141: Display the Head of a File

from sys import argv

# must mention script here, so python wouldn't confuse it for an argument
try:
	script, filename = argv
except ValueError:
	print "No file given as an argument."
	exit()

try:
	txt = open(filename)
except IOError:
	print "File doesn't exist."
	exit()

for i in range(10):
	print txt.readline(), # without comma, for some reason it puts empty line between each line

