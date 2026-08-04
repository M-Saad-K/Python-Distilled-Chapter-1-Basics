import os

filename = 'stock.txt'
rows = []

if os.path.exists(filename):
    with open(filename, 'rt') as file:
        for line in file:
            rows.append(line.split(','))
            print(rows)
else:
    raise SystemExit(f"{filename} couldn't be found")


total = sum([int(row[1]) * float(row[2]) for row in rows])
print(f"Total cost is {total:0.2f} ")