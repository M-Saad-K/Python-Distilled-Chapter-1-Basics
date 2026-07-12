"""
@ Author: Muhammad Saad Khan
@ Date: 11 - 07 - 2026
@ Name: Part1.py
@ Version: Python 3.12.3 on Linux

Description:

This page covers task from 1.1 -> 1.6
"""

import sys

def main():
    practise7()



def practise0():
    # Primitive
    x = 42
    b : int = 42
    y = 4.2
    z = 'forty-two'
    a = True

    i: int = 0

    # While

    while i <= 4:
            print("This is i: ", i)
            i=i+1


def practise1():
    prin: int = 1000
    rate: float = 0.05
    numyears: int = 5
    year: int = 1

    while year < numyears:
        prin = prin * (rate + 1)
        print(year, prin)
        year+=1

def practise2():
    # Bit Manipulation
    x : int = 1
    print(x << 1) # Left shift goes up
    print(x >> 1) # Right shift goes down

    """
        3          =>  00011
      & 5          =>  00101
    ------           -------
        1              00001
    """
    # bitwise and, if two areas have 1, then 1
    print(12 & 20)
    # | ^ -x (or, xor, neg)
    y = 100001
    print(f"y shift 5 times is to the right {y >> 5}")

def practise3():
    a: int = 0
    b: int = 5

    while True:
        if a < b:
            print("Yes")
        else: 
            print("No")
            break
        a+=1

    while True: # This is a bad infinite example
        suffix = '.htm'
        if suffix == ".htm":
            content = 'text/html'
            suffix = '.jpg'
            print(content)
        elif suffix == '.jpg':
            content = 'image/jpeg'
            print(content)
            suffix= "Laika"
        else: 
            raise RuntimeError(f"Unknown content type {suffix!r}")

def practise4():
    # Combinatory assignment
    a: int = 0
    b: int = 1
    x = a if a > b else b
    print("X is", x)

    # Walrus op, this is assignment based on combinatory logic
    y = 0
    while (y := y + 1) < 10:
        print("Y is", y)
        
    suffix = '.htm'
    
    # There is a continue that goes back to the top of the loop
    while True: # This is a bad infinite example
        
        if suffix == ".htm":
            content = 'text/html'
            suffix = '.jpg'
            print(content)
            continue
        elif suffix == '.jpg':
            content = 'image/jpeg'
            print(content)
            suffix= "Laika"
            continue
        else: 
            raise RuntimeError(f"Unknown content type {suffix!r}")

def practise5():
    # For decimal
    gravity: float = 9.89999
    print(f"This is round {gravity:.2f}")

def practise6():
    # Char array
    greeting: str = "Hello my name is Saad and I study CES at Strathclyde"
    print(len(greeting))
    b = greeting[4]
    print(b)
    e = greeting[3:10]
    print(e)
    greeting = greeting.replace('Saad', 'Laika')
    print(greeting)

def practise7():
    sentence: str = "The big brown rabbit jumped over the red fox" 
    print(sentence.endswith("fox", 41, 44))
    print(sentence.find("rabbit"))
    newSent = sentence.split(" ", 4)
    print(newSent)
    # strip removes an trailing whitespace
    #  format as strings using str() and repr()
    x: int = 5
    forcast: str = "Weather is " + str(x) + "*c\nGlasgow, Scotland"
    print(forcast)

if __name__ == '__main__':
    main()