import sys
numPeople, numEdges = [int(x) for x in sys.stdin.readline().split()]
adjacencyList = [[] for x in range(numPeople+1)]
for i in range(numEdges):
    x, y = [int(x) for x in sys.stdin.readline().split()]
    # person x is taller than person y
    # so the graph has arrows pointing from x to y
    adjacencyList[x].append(y)
a, b = [int(x) for x in sys.stdin.readline().split()]

def bfs(start, finish):
    visited = [False]*(numPeople+1)
    queue = [[start]]
    while queue:
        currpath = queue.pop(0)
        if currpath[-1] == finish:
            return True
        if not visited[currpath[-1]]:
            visited[currpath[-1]] = True
            for person in adjacencyList[currpath[-1]]:
                newpath = list(currpath)
                newpath.append(person)
                queue.append(newpath)
    return False
if bfs(a, b):
    print("yes")
else:
    if bfs(b, a):
        print("no")
    else:
        print("unknown")
