
def read_portfolio(filename):
    portfolio : int = []

    with open(filename) as file:
        for line in file:
            row = line.split(", ")
            for word in row:
                portfolio.append(word)

    return portfolio
