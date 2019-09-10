#By Cade & Aidan
#Sentence Writer

import time

i = 0

while i == 0:

    print("Type your sentence: ")

    text = input()

    wordArray = text.split()

    numWord = len(wordArray)

    for x in range(0, numWord):
        word = wordArray[x]
        numLetter = len(word)
        for y in range (0, numLetter):
            letter = word[y]
            print(letter)
        print("-")
    print(" ")
    i = 0
