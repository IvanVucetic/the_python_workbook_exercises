# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 87
# Date: 03.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 87: Center a String in the Terminal

def centered(string, width):
	leading = (width/2 - len(string)/2) * " "
	string2 = leading + string

	print string2

text = "Some testing-purposes string."
text2 = "I could try out more than one string."

#	terminal width- command "tput cols" in the terminal
centered(text, 152)
centered(text2, 152)