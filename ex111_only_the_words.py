# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 111
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 111: Only the Words

def split_2_words(string):
	li = string.split()
	li_s = []
	for i in li:
		li_s.append(i.strip("!.,:;?\'\"-"))
	return li_s

def main():
	print "Insert a string:"
	s = raw_input("> ")
	print split_2_words(s)

if __name__ == "__main__":
	main()
