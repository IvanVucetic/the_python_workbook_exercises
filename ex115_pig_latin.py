# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 115
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 115: Pig Latin

print "Enter a sentence:"
string = raw_input("> ")

li = string.split()
li_pig = []

for word in li:
	if word[0] in "aeiouy":
		li_pig.append(word + "way")
	else:
		for i in range(len(word)):
			if word[i] in "aeiouy":
				li_pig.append(word[i:]+word[:i]+"ay")
				break #otherwise it makes all combinations of the word

print " ".join(li_pig)