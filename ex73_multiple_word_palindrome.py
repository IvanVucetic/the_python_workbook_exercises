# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 73
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 73: Multiple Word Palindromes

print "Insert a sting:"
words = raw_input("> ").lower() # into lowercase to ease the comparison
words = "".join(words.split())	# remove spaces
words = words.translate(None, "!?.,")	# remove chars given as argument

match = "is"
for i in range(0, len(words)):
	if words[i] != words[-(i+1)]: # compares word[0] == word[-1] and so on
		match = "isn't"
	else:
		pass

print "The expression %s a palindrome." % match