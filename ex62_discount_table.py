# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 62
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 62: Discount Table

prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for price in prices:
	disc = price * 0.6
	new_price = price * 0.4
	print "price: %s, discount: %.2f, new price: %.2f" % (price, disc, new_price)