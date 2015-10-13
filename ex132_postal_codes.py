# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 132
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 132: Postal Codes

province = {'A': 'Newfoundland', 'B':'Nova Scotia', 'C':'Prince Edward Island',\
            'E':'New Brunswick', 'G':'Quebec', 'H':'Quebec', 'J':'Quebec',\
            'K':'Ontario', 'L':'Ontario', 'M':'Ontario', 'N':'Ontario',\
            'P':'Ontario', 'R':'Manitoba', 'S':'Saskatchewan', 'T':'Alberta',\
            'V':'British Columbia', 'X':'Nunavut or Northwest Territories',\
            'Y':'Yukon'}

code = raw_input('Insert postal code: ')
if code[0] not in province.keys() or len(code) != 7:
    print "Not a valid postal code!"
    exit()

area = 'a rural' if code[1] == '0' else 'an urban'

print "The code is for %s address in %s." % (area, province[code[0]])
