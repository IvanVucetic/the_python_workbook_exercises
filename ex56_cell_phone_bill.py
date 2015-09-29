# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 56
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 56: Cell Phone Bill

print "Enter a number of spent minutes:"
minutes = int(raw_input("> "))
print "Enter a number of spent messages:"
sms = int(raw_input("> "))

add_min = minutes - 50 if minutes > 50 else 0
add_sms = sms - 50 if sms > 50 else 0

base_charge = 15.00
charge_911 = 0.44
tax = (base_charge + charge_911 + add_min*0.25 + add_sms*0.15) * 0.05
total_charge = (base_charge + charge_911 + add_min*0.25 + add_sms*0.15) * 1.05

print type(add_min), type(add_sms)

print "Base charge: $%.2f." % base_charge
if add_min != 0:
    print "Additional minutes: $%.2f." % (add_min*0.25) #must go inside ()
if add_sms != 0:
    print "Additional messages: $%.2f." % (add_sms*0.15) #must go inside ()
print "Charge for 911 services: $%.2f." % charge_911
print "Tax: $%.2f." % tax
print "Total charge: $%.2f." % total_charge