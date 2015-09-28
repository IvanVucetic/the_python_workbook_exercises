# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 36
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 36: Vowel or Consonant

print "Enter a letter of the alphabet:"
letter = raw_input("> ")

if letter in ('a', 'e', 'i', 'o', 'u'):
	print "%s is a vowel." % letter
elif letter == 'y':
	print "y is sometimes vowel, sometimes consonant."
else:
	print "%s is a consonant." % letter