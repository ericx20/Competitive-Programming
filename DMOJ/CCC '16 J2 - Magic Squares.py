import sys
square = []
for i in range(4):
    square.append([int(x) for x in sys.stdin.readline().split()])
magicSum = sum(square[0])
magic = True
for row in square:
    if sum(row) != magicSum:
        magic = False
for i in range(4):
    columnSum = 0
    for row in square:
        columnSum += row[i]
    if columnSum != magicSum:
        magic = False
if magic:
    print("magic")
else:
    print("not magic")
