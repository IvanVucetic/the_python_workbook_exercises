# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 129
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 129: Two Dice Simulation

def roll_dice():
    # we must have 2 dice 1-6, not just one 2-12, or percentage won't match
    from random import randint
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1 + d2

def main():
    expected = {2:1/36.0, 3:2/36.0, 4:3/36.0, 5:4/36.0, 6:5/36.0, 7:6/36.0, 8:5/36.0, \
                9:4/36.0, 10:3/36.0, 11:2/36.0, 12:1/36.0}

    # dict to hold number of scores for each total; init. 2:0, 3:0...12:0
    rolls = {}
    for i in range(2,13):
        rolls[i] = 0

    for i in range(1000):
        total = roll_dice()
        rolls[total] += 1

    print rolls

    print "Total    Simulated    Expected"
    print "          Percent      Percent"
    for i in rolls:
        print "%3d %11.2f %12.2f" % (i, rolls[i]/1000.0 * 100, expected[i]*100)

main()