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
