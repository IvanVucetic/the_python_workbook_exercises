# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 128
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 128: Reverse Lookup

def reverseLookup(dictio, value):
	keys = []
	for k,v in dictio.items():
		if v == value:
			keys.append(k)

	return keys

def main():
	a = {'a': 1, 'b': 2, 'c': 1}
	print reverseLookup(a,1)
	print reverseLookup(a,2)
	print reverseLookup(a,3)

if __name__ == "__main__":
	main()

