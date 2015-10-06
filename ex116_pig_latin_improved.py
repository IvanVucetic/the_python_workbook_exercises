# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 116
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 116: Pig Latin Improved

import string

print "Enter a sentence:"
string_ = raw_input("> ")

li = string_.split()
li_pig = []

for word in li:
    # handle punctuation if any
    punc = ""
    if word[-1] in string.punctuation:
        punc = word[-1]
        word = word[:-1]
    # first  if starts with vocal, second  if starts with consonant
    if word[0] in "aeiouy":
        li_pig.append(word + "way" + punc)
    # starts with uppercase vocals
    elif word[0] in "AEIOUY":
        li_pig.append((word + "way" + punc).capitalize())
    # uppercase consonants
    elif word[0] in string.uppercase.translate(None, 'AEIOUY'): #upper conson.
        for i in range(len(word)):
            if word[i] in "aeiouy":
                new_word = word[i:]+word[:i]+"ay" + punc
                li_pig.append(new_word.capitalize())
                break #otherwise it makes all combinations of the word
    else:
        for i in range(len(word)):
            if word[i] in "aeiouy":
                li_pig.append(word[i:]+word[:i]+"ay" + punc)
                break #otherwise it makes all combinations of the word

print " ".join(li_pig)