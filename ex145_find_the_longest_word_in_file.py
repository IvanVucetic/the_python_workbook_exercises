# Ben Stephenson - The Python Workbook
#
# Exercise no. 144
# Date: 19.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 145: Find the Longest Word in a File

from sys import argv

if len(argv) != 2:
	print "Give one file with text as an argument."
	exit()

txt = open(argv[1], 'r')
# set maximum to 0 and make en empty list of longest words
m = 0
longest = []

for line in txt:
	line = line.split(" ") # otherwise it doesnt look at separate words, but letters
	for word in line:
		if len(word) == m:
			longest.append(word)
		elif len(word) > m:
			m = len(word)
			longest = []
			longest.append(word)
		else:
			pass

print "The length of the longest word is", m
print "There are %i such words:" % len(longest)
print longest

