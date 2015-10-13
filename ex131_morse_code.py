# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 131
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 131: Morse Code

code = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',\
        'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',\
        'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.',\
        's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',\
        'y':'-.--', 'z':'--..', '0':'-----', '1':'.----', '2':'..---',\
        '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',\
        '8':'---..', '9':'----.'}

msg = raw_input("Insert message: ")
msg = msg.lower()
output = ""

for symbol in msg:
    if symbol in code.keys():
        output = output + code[symbol] + " "
    else:
        pass

print output