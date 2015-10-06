# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 119
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 119: Dealing Hands of Cards

def deal(hands,cards_ph,deck):
	dealt = []
	for h in range(hands):
		dealt.append([])

	for card in range(cards_ph):
		for hand in dealt:
			hand.append(deck.pop())

	return dealt

def main():
	from ex118_shuffling_deck_of_cards import create_deck, shuffle
	deck = create_deck()
	shuffled = shuffle(deck)

	print deal(4,5,shuffled)
	print shuffled

main()