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
