import sys
numHouses, numRoads, a, b = [int(x) for x in sys.stdin.readline().split()]
adjacency =[[] for x in range(numHouses+1)]
for q in range(numRoads):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    adjacency[x].append(y)
    adjacency[y].append(x)
def bfs(start, finish):
    visited = [False for x in range(numHouses+1)]
    queue = [[start]]
    while queue:
        currpath = queue.pop(0)
        if currpath[-1] == finish:
            return True
        if not visited[currpath[-1]]:
            visited[currpath[-1]] = True
            for house in adjacency[currpath[-1]]:
                newpath = list(currpath)
                newpath.append(house)
                queue.append(newpath)
    return False
if bfs(a, b):
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")
