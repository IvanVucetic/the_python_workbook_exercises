# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 137
# Date: 14.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 137: Scrabble Score

score = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,\
		 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
		 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

word = raw_input("Insert a word: ").lower()
total = 0
for letter in word:
	total += score[letter]

print total