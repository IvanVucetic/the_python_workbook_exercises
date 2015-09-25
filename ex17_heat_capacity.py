# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 17
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 17: Heat Capacity

print "Mass of water you want to heat-up/cool-down in grams:"
while True:
	m = float(raw_input("> "))
	if m > 0:
		break
	else:
		print "Must be positive number"

print "Desired temperature difference in degrees Celsius:"
d_temp = float(raw_input("> "))

cap = 4.186 # Joules per (gram * degree C)

q_joules = m * cap * d_temp
print "Requred energy for the change is %.2f Joules" % q_joules

q_kWh = q_joules / 3600000
price = q_kWh * 8.9

print "The cost of the change is %.2f cents." % price