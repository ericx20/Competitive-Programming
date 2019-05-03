flips = input()
grid = [[1, 2,], [3, 4]]
numH = flips.count("H")
numV = flips.count("V")
if numH % 2 == 1:
    grid = grid[1], grid[0]
if numV % 2 == 1:
    grid = [grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]
for row in grid:
    print(row[0], row[1])
