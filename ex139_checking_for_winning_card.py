# Ben Stephenson - The Python Workbook
#
# Exercise no. 139
# Date: 15.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 139: Checking for a Winning Card

def checkWinner(card):
    summ = 0
    winner = False

    # check vertically- if all under 'b', or all under 'i'...
    for letter in 'bingo':
        if sum(card[letter]) == 0:
            winner = True

    # horizontally- b[1]==0 and i[1]==0 and... 0[1]==0
    for i in range(5):
        summ = 0
        for letter in 'bingo':
            summ += card[letter][i]
        if summ == 0:
            winner = True
            break

    # diagonally- b[0] to o[4], or b[4] to o[0]
    if card['b'][0] == 0:
        i = 0
        summ = 0
        for l in 'bingo':
            summ += card[l][i]
            i += 1
        if summ == 0:
            winner = True
    elif card['b'][4] == 0:
        i = 4
        summ = 0
        for l in 'bingo':
            summ += card[l][i]
            i -= 1
        if summ == 0:
            winner = True

    return winner


def main():
    from ex138_create_bingo_card import displayBingoCard
    
    card1 = {'b':[1,1,1,1,0], 'i':[1,1,3,0,1], 'n':[1,1,0,1,1], 'g':[1,0,5,1,1], 'o':[0,9,9,9,1]}
    print "diagonal:"
    displayBingoCard(card1)
    print "Winner!" if checkWinner(card1) else "Loser!"

    card2 = {'b':[1,1,1,1,0], 'i':[1,1,3,1,0], 'n':[1,1,1,1,0], 'g':[1,1,5,1,0], 'o':[1,9,9,9,0]}
    print "horizontal:"
    displayBingoCard(card2)
    print "Winner!" if checkWinner(card2) else "Loser!"

    card3 = {'b':[1,1,1,1,0], 'i':[1,1,3,1,1], 'n':[0,0,0,0,0], 'g':[1,1,5,1,1], 'o':[1,9,9,9,1]}
    print "vertical:"
    displayBingoCard(card3)
    print "Winner!" if checkWinner(card3) else "Loser!"

    card4 = {'b':[1,1,1,1,0], 'i':[1,0,3,1,1], 'n':[1,1,1,1,0], 'g':[1,0,5,1,1], 'o':[1,9,9,9,1]}
    print "not a winner:"
    displayBingoCard(card4)
    print "Winner!" if checkWinner(card4) else "Loser!"

main()