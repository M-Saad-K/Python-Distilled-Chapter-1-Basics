import sys

def main():

    read_portfolio(trades.txt)


def read_portfolio(filename):
    portfolio : int = []

    with open(filename) in file:
        for line in file:
            row = line.split(", ")
            for word in row:
                portfolio.append(word)

    return portfolio