# Ben Stephenson - The Python Workbook
#
# Exercise no. 140
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 140: Play Bingo
from random import shuffle
from ex138_create_bingo_card import createBingoCard, displayBingoCard
from ex139_checking_for_winning_card import checkWinner


def generateCalls():
	calls = []
	# all possible calls:
	start = 1
	for l in 'bingo':
		for i in range(start, start+15):
			calls.append(str(l)+str(i)) #should concat l and i
		start += 15
	shuffle(calls)
	return calls


def playBingo():
	calls = generateCalls()
	num_calls = 0
	card = createBingoCard()
	displayBingoCard(card)
	
	while True: #play until there is a winner
		new_call = calls.pop()
		print "New call:", new_call
		call_l = new_call[0]
		call_n = int(new_call[1:])
		num_calls += 1
	
		if call_n in card[call_l]:
			print "The number is on your card."
			# card[call_l] is a list; switch call_n value from that list with 0
			# n is a location of that value in the list
			for n, v in enumerate(card[call_l]):
				if v == call_n:
					card[call_l][n] = 0
			displayBingoCard(card)
			if checkWinner(card):
				print "WIN!"
				break
		else:
			print "Not on your card!"
	
	print "Number of calls:", num_calls
	return num_calls


def main():
	min_calls = 9999 #min number of calls for card to win
	max_calls = 0 #max number of calls for card to win
	sum_calls = 0 #total

	for i in range(1000):
		num_calls = playBingo()
		sum_calls += num_calls
		if num_calls > max_calls:
			max_calls = num_calls
		if num_calls < min_calls:
			min_calls = num_calls

	print "Maximum number of calls to win a card:", max_calls
	print "Minimum number of calls to win a card:", min_calls
	print "Average number of calls to win a card:", sum_calls/1000


main()
