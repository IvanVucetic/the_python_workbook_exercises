# Ben Stephenson - The Python Workbook
#
# Exercise no. 144
# Date: 19.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 146: Letter Frequencies

from sys import argv
import string

if len(argv) != 2:
	print "Wrong number of command-line arguments."
	quit()

try:
	txt = open(argv[1], 'r')
except IOError:
	print "Cannot open file", argv[1]

# create a dict to store occurences of letters
d = {}
for i in string.lowercase:
	d[i] = 0

for line in txt.readlines():
	for word in line:
		# turn all to lowercase, to make it case-insensitive
		word = word.lower()
		# check if it is a letter and not number or punctuation
		if word in string.lowercase:
			d[word] += 1

print d