import sys
# input trees
numTrees = int(sys.stdin.readline())
treeList = [0]
for counter in range(numTrees):
    treeList.append(int(sys.stdin.readline()))
# generate prefix  sum array
prefixSum = [0]
for i in range(1, len(treeList)):
    prefixSum.append(treeList[i] + prefixSum[i-1])
# input and answer queries instantaneously
numQueries = int(sys.stdin.readline())
for counter in range(numQueries):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    print(prefixSum[b + 1] - prefixSum[a])
