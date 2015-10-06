# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 118
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 118: Shuffling a Deck of Cards

def create_deck():
	values = [2,3,4,5,6,7,8,9,"T","J","Q","K","A"]
	suits = ['s','h','d','c']
	cards = []

	for v in values:
		for s in suits:
			cards.append(str(v)+s)

	return cards

def shuffle(deck):
	from random import randint
	for i in range(len(deck)):
		rand = randint(0,51)
		x = deck[i]
		deck[i] = deck[rand]
		deck[rand] = x

	return deck

def main():
	if __name__ == "__main__":
		deck = create_deck()
		print deck
		print shuffle(deck)

main()



