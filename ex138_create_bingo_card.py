# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 136
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 138: Create a Bingo Card

def createBingoCard():
	from random import sample
	vals = {'b':[], 'i':[], 'n':[], 'g':[], 'o':[]}

	# using sample instead of randint to get unique values
	vals['b'] = sample(range(1,15),5)
	vals['i'] = sample(range(16,30),5)
	vals['n'] = sample(range(31,45),5)
	vals['g'] = sample(range(46,60),5)
	vals['o'] = sample(range(61,75),5)

	return vals

def displayBingoCard(values):
	print " B  I  N  G  O"
	for i in range(5):
		print "%2i %2i %2i %2i %2i" % (values['b'][i], values['i'][i], \
			values['n'][i], values['g'][i], values['o'][i])


def main():
	if __name__ == '__main__':
		card = createBingoCard()
		displayBingoCard(card)

main()

