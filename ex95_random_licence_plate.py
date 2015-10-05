# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 95
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 95: Random License Plate

def plate_generator():
	from random import randint

	if randint(0,1) == 0:
		old = ""
		for i in range(3):
			old = old + chr(randint(65,90))
		for i in range(3):
			old = old + str(randint(0,9))
		print old
	else:
		new = ""
		for i in range(4):
			new = new + str(randint(0,9))
		for i in range(3):
			new = new + chr(randint(65,90))
		print new

def main():
	plate_generator()

if __name__ == "__main__":
	main()




