numOfLines, numOfJoining = input().split()
numOfLines = int(numOfLines)
numOfJoining = int(numOfJoining)
lineList = [int(x) for x in input().split()]
lineList.sort()
for i in range(numOfJoining):
    print(lineList[0])
    lineList[0] += 1
    lineList.sort()
