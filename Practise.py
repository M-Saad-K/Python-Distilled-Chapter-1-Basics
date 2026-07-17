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
    practise14()



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
    forcast: str = "                           Weather is " + str(x) + "*c\nGlasgow, Scotland                                                                    "
    print(forcast.strip())

def practise8():

    data: str = " "

    ### This is for each line

    with open('input.txt') as file: #Open func returns a file object
        # The with statement is used to not have to close it again
        for line in file: # For each line in the file
            print(line, end='') # Print each line, omitting the extra newline


    ### This is for entirity
    with open('input.txt') as file:
        data = file.read()
        print(data)

    ### large file in chunks, for larger files, you can assign them
    # The chunk will read for 4 blocks
    with open('input.txt') as file:
        while(chunk := file.read(4)): # The := assigns a value and returns a value for the while loop to use as well
            print(chunk, end='')


    # Outputting to a file
    data = data.replace("Moon", "ISS")
    with open('output.txt', 'wt') as output: # wt is writing
        # print(data, file=output) # But printing is for additional words using while, like the example on pg13
        output.write(data)
    
    name = input("What is your name: ")
    print(name)

def practise9():
    arr: int = [1, 2, 4, 5]
    #End of list
    arr.append(6)
    # Any point
    arr.insert(2, 9)

    # Turn into list
    daveBroke = list('Dave')
    
    for i in arr:
        print(i)

    print(daveBroke)
    
def practise10():
    # Nested list
    objectList  = [1, 'Dave', ['Mark', 7, 9, [100, 101]], 10]
    print(objectList[1])
    print(objectList[2][0])
    print(objectList[2][3][1])

def practise11():
    # tuple is done using (), not [], can't change
    holding = ('GOOG', 100, 480.10)
    address = ('www.python.org', 80)
    onlyOneElementTuple = (1,)
    emptyTuple = ()

    # Assign to variables
    stock, shares, price = holding
    url, id = address

def practise12():
    portfolio = []
    total: float = 0.0
    with open("stock.txt") as file:
        for line in file:
            row = line.split(',')
            name = row[0]
            noShare = row[1]
            priceP = row[2]
            holdings = (name, noShare, priceP)
            portfolio.append(holdings)
            for name, noShare, priceP in portfolio:
                total += (int(noShare) * float(priceP))
    print(portfolio, total)

def practise13():
    # Sets, order is not predicted, and things can only appear once, and unpredicted position
    portfolio = ("Art", "Part", "Cart", "Part")
    # Return all the elements into set
    names = {i for i in portfolio}
    #print(names)

    jobs = {"Art", "Lark", "Bark"}

    names.add('Mark')
    jobs.update({'Cart', 'Part', 'Mart'}) # need braces
    names.remove('Art')

    # Comparing set elements
    print(names | jobs)
    print(names & jobs)
    print(names - jobs) 
    print(jobs - names)
    print(names ^ jobs) # Either but not both

def practise14():
   # Dicitonaries
   s = {
        'name' : 'AAPL',
        'shares' : 100,
        'prices' : 490.10
   }

   name = s['name'] # Must reference the name of the dictionary
   print(name)

   s['shares'] = 1249.80

   p = 1

   if 'prices' in s:
        p = s['prices']
   else:
        p = 0.0

   # or write this
   p = s.get('prices', 0.0) # Get prices or 0.0
   print("p =", p)

   del s['name'] # removing elements
   print(s)

   portfolio = {
        ('GOOG', 1.8, 300),
        ('AAPL', 5.6, 320),
        ('NVID', 2.1, 567) }
   total_shares = {s[0]: 0 for s in portfolio}
   for names, shares, _ in portfolio:
        total_shares[names]+= shares
   print(total_shares)
   # Get keys
   print(total_shares.keys())

def practise15():
    return
if __name__ == '__main__':
    main()