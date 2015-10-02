# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 72
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 72: Is a String a Palindrome?

print "Insert a sting:"
word = raw_input("> ").lower() # into lowercase to ease the comparison


match = "is"
for i in range(0, len(word)):
	if word[i] != word[-(i+1)]: # compares word[0] == word[-1] and so on
		match = "isn't"
	else:
		pass

print "The word %s a palindrome." % match
