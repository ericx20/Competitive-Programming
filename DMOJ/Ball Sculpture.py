import sys
numSwitches, numBalls = [int(x) for x in sys.stdin.readline().split()]
switchCounter = [0]*(numSwitches+2)
switchCounter[1] = numBalls
for i in range(1, numSwitches+1):
    outputTracks = [int(x) for x in sys.stdin.readline().split()]
    switchCounter[outputTracks[0]] += (switchCounter[i]+1)//2
    switchCounter[outputTracks[1]] += switchCounter[i]//2
    switchCounter[i] = switchCounter[i]%2
print(''.join(str(x) for x in switchCounter[1:numSwitches+1]))
