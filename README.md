# Aidan & Cade's Engineering 4 Notebook

1) [Introductory Projects](https://github.com/ADaMiller14/Engineering_4_Notebook#raspberry-pi)
    - 1.1 [Hello Raspberry Pi Zero](https://github.com/ADaMiller14/Engineering_4_Notebook#hello-raspberry-pi-zero)
    - 1.2 [Hello Mathematica](https://github.com/ADaMiller14/Engineering_4_Notebook#hello-mathematica)
  
2) [Python Projects](https://github.com/ADaMiller14/Engineering_4_Notebook#python)
    - 2.1 [Hello Python](https://github.com/ADaMiller14/Engineering_4_Notebook#hello-python)
    - 2.2 [Calculator](https://github.com/ADaMiller14/Engineering_4_Notebook#calculator)
    - 2.3 [Quadratic Solver](https://github.com/ADaMiller14/Engineering_4_Notebook#quadratic-solver)
    - 2.4 [Strings and Loops](https://github.com/ADaMiller14/Engineering_4_Notebook#strings-and-loops)
    - 2.5 [MSP](https://github.com/ADaMiller14/Engineering_4_Notebook#hangman)

3) [GPIO](https://github.com/ADaMiller14/Engineering_4_Notebook#GPIO)
    - 3.1 [Bash](https://github.com/ADaMiller14/Engineering_4_Notebook#Bash)
    - 3.2 [Python](https://github.com/ADaMiller14/Engineering_4_Notebook#Python)
    - 3.3 [SSH](https://github.com/ADaMiller14/Engineering_4_Notebook#SSH)
    - 3.4 [12C](https://github.com/ADaMiller14/Engineering_4_Notebook#12C)
  
4) [Flask & Son](https://github.com/ADaMiller14/Engineering_4_Notebook#Flask-&-Son)
    - 4.1 [Hello Flask](https://github.com/ADaMiller14/Engineering_4_Notebook#Hello-Flask)
    - 4.2 [Hydro Flask](https://github.com/ADaMiller14/Engineering_4_Notebook#Hydro-Flask)

5) [Big Boi Projects](https://github.com/ADaMiller14/Engineering_4_Notebook#Big-Boi-Projects)
    - 5.1 [Headless](https://github.com/ADaMiller14/Engineering_4_Notebook#Headless)
    - 5.2 [Pi Camera](https://github.com/ADaMiller14/Engineering_4_Notebook#Pi-Camera)
    - 5.3 [Hack Your Stuff](https://github.com/ADaMiller14/Engineering_4_Notebook#Hack-Your-Stuff)
    - 5.4 [Copypasta](https://github.com/ADaMiller14/Engineering_4_Notebook#Copypasta)
___
## Introductory Projects
### Hello Raspberry Pi Zero
This was an introduction to pi and, more specifically, bash scripts.

<details>
<summary>Code</summary>
<br>
    <pre>
#!/bin/bash
str="Hello World!" #declares the string
for i in {1..10} #run the loop 10 times
done
</pre>
</details>

### Hello Mathematica
This project was trying to figure out how to write a line of Mathematica to make a plot with sliders

Unfortunately we did not push the code to github
### Hello Git
We set up Github on the pi.
### Git Forks and Clones
We forked a repository (class accounts) and cloned it to the pi. After, we added our names to it then committed it.
## Python
### Hello Python
This project was a dice roller. It's basically a RNG for the numbers 1-6.

<details>
<summary>Code</summary>
<br>
    <pre>
# Automatic Die Roller
# Written By Aidan Miller & Cade Young

import random
from random import randint

print ("Automatic D6 Roller")
print ("Press Enter to roll, press x to exit")

x = 0

while x == 0:
    if input() == "":
        r1 = random.randint(1,6)
        print((r1))
        print("Roll again?")
    if input() == "x":
        exit()
</pre>
</details>
</details>

### Calculator
Our task was to "Write a program that gives you the sum, difference, quotient, and modulo of the two numbers" in Python.

<details>
<summary>Code</summary>
<br>
    <pre>
# By Aidan & Cade
# Calculator

import time

def doMath(n1, n2, n3):
    if n2 == "+":
        return (int(n1) + int(n3))
    if n2 == "-":
        return (int(n1) - int(n3))
    if n2 == "*":
        return (int(n1) * int(n3))
    if n2 == "/":
        return (round(int(n1) / int(n3), 2))
    if n2 == "%":
        return (int(n1) % int(n3))
    else:
        return ("Error")

#----------------------------------------

m1 = 0
m2 = 0
m3 = 0

x = 0

print("Welcome to Calculator!")
time.sleep(1)

while x == 0:
    print("Write your equation, one part at a time")
    time.sleep(1)

    print("What is the first term?")
    m1 = input()

    print("What is the operation?")
    m2 = input()

    print("What is the second term?")
    m3 = input()

    print()
    time.sleep(1)
    print((m1) + " " + (m2) + " " + (m3) + " = " + str(doMath((m1), (m2), (m3))))
    print("")

    if doMath((m1), (m2), (m3)) == "Error":
        print("Goodbye")
        exit()
</pre>
</details>

### Quadratic Solver
Forgive me if I go too fast. We made, as the title suggests, a program to solve quadratics. 
<details>
<summary>Code</summary>
<br>
    <pre>
# By Aidan & Cade
# Quadratic Solver

import time
import math

def quadDis(a, b, c):

    roots = []
    
    d = (math.pow(int(b), 2) - (4 * int(a) * int(c)))
    
    if d < 0:
        return("No real roots")

    if int(a) == 0:
        return("Undefined")

    else:
        roots.append(((-int(b) + math.sqrt( math.pow(int(b), 2) - 4 * int(a) * int(c) )) / (2 * int(a))))
        roots.append(((-int(b) - math.sqrt( math.pow(int(b), 2) - 4 * int(a) * int(c) )) / (2 * int(a))))
        return(roots)

#-------------------------------------------------------

a = 0
b = 0
c = 0

x = 0

print("Quadratic Solver")

while x == 0:
    time.sleep(.5)
    print("Enter the coefficients for ax^2 + bx + c = 0")

    print("")
    print("a = ")
    a = input()
    time.sleep(.1)

    print("")
    print("b = ")
    b = input()
    time.sleep(.1)

    print("")
    print("c = ")
    c = input()
    time.sleep(.1)

    print("")
    if a == "1":
        print("x^2 + " + (b) + "x + " + (c) + " = 0")
    else:
        print((a) + "x^2 + " + (b) + "x + " + (c) + " = 0")
        
    print("x = " + str(quadDis((a), (b), (c))))

    print("")
</pre>
</details>

### Strings and Loops
This one was a bit of a doozie. It was tricky because we needed to split strings up.
<details>
<summary>Code</summary>
<br>
    <pre>
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
</pre>
</details>

### MSP 
The Man Shaped Pinata

Oh boy was this trouble. This project took a long time and set us back quite a bit. However, if you'll notice, we brought in unicode characters to  make it all look better so that's a plus.
<details>
<summary>Code</summary>
<br>
    <pre>
#By Aidan & Cade
#Hangman

def hangmanPrint(x):
    if int(x) == 0:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("\n" * 6)
    if int(x) == 1:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u263A")
        print("\n" * 5)
    if int(x) == 2:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u263A")
        print("  |")
        print("\n" * 4)
    if int(x) == 3:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u263A")
        print(" /|")
        print("/")
        print("\n" * 3)
    if int(x) == 4:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u263A")
        print(" /|" + "\\" + "/")
        print("/")
        print("\n" * 3)
    if int(x) == 5:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u263A")
        print(" /|" + "\\" + "/")
        print("/ |")
        print("  " + u"\u039B")
        print("\n" * 2)
    if int(x) == 6:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u263A")
        print(" /|" + "\\" + "/")
        print("/ |")
        print("  " + u"\u039B")
        print(" " + "/" + " ")
        print("")
    if int(x) == 7:
        print(u"\u2501" + u"\u2501" + u"\u2511")
        print("  " + u"\u2639")
        print(" /|" + "\\" + "/")
        print("/ |")
        print("  " + u"\u039B")
        print(" " + "/" + " " + "\\")
        print("You lose!")
    if int(x) < 0 or int(x) > 7:
        print("Error: Bad Hangman Value")

#-------------------------------------

def hangmanCheck(w, g):
    if str(g) in str(w):
        return(0)
    else:
        return("1")
    
#-------------------------------------

def hangmanWord(w, a):
    guessArray.append(a)
    val = 0
    for x in listArray:
            if x not in guessArray:
                val = val + 1
    if val == 0:            
        print(w)
        print("Letters guessed:" + str(letterArray))
        print("Player 2 wins!")
        exit()
    else:
        for x in listArray:
            if x in guessArray:
                print(x + " ", end='')
            else:
                print(u"\u203F" + " ", end='')

#--------------------------------------

cutscene = 0
word = "0"
yn = "0"
guess = "0"
man = 0
letterArray = []
guessArray = [" "]
listArray = []
val = 0

print("Welcome to Hangman!")

while cutscene == 0:
    print("Player 1, what's your word?")
    word = input()
    word.lower()
    listArray.clear()
    for y in word:
        listArray.append(y)
    print("Your word is " + word + ", right? Write Y or N.")
    yn = input()
    if yn == "Y":
        cutscene = 1
    else:
        if yn == "N":
            print("Whoops")
        else:
            print("huh?")

while cutscene == 1:
    print("\n" * 40)
    hangmanPrint(man)
    hangmanWord(word, guess)
    print()
    print("Letters guessed:" + str(letterArray))
    if man == 7:
        print("Player 1 wins!")
        print("The word was " + word + "!")
        exit()
    if man < 7:
         print("Player 2, guess a letter")
    guess = input().lower()
    letterArray.append(str(guess))
    letterArray.sort()
    if hangmanCheck(word, guess) == "1":
        if man < 7:
            man = man + 1
</pre>
</details>

## GPIO 
Green Potatoes in Onions
### Bash
stuff
### Python
stuff
### SSH
stuff
### 12C
stuff
## Flask & Son
### Hello Flask
stuff
### Hydro Flask
stuff
## Big Boi Projects
Putting the stuff together
### Headless 
spanish inquisition?
### Pi Camera 
we see you
### Hack Your Stuff 
we see you more now
### Copypasta 
how'd the italian chef die? He copypasta way
