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
