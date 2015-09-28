# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 33
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 33: Day Old Bread

print "Insert a number of loaves that you wish to buy:"
num_ = int(raw_input("> "))

price = 3.49
disc = 0.6 * price

reg_price = num_ * price
tot_disc = num_ * disc
tot_price = reg_price - tot_disc

print "Regular price: %.2f" % reg_price
print "Discount: %.2f" % tot_disc
print "Total: %.2f" % tot_price

# couldn't make Author's solution for aligning work for me