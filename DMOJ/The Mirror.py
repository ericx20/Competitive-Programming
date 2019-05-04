import math
def checkPrime(n):
    #print("Checking", n)
    if n in [0, 1]:
        #print("0 or 1 is not prime")
        return False
    elif n == 2:
        return True
    else:
        isPrime = True
        for divisor in range(2, math.ceil(math.sqrt(n))+1):
            if n%divisor == 0:
                #print("Factor found!", divisor)
                isPrime = False
                break
        #print("Is", n, "prime?", isPrime)
        return isPrime
numOfCases = int(input())
answerList = []
for caseNum in range(numOfCases):
    numOfPrimes = 0
    intervalList = input().split(" ")
    interval = range(int(intervalList[0]), int(intervalList[1]))
    for num in interval:
        if checkPrime(num):
            numOfPrimes += 1
    answerList.append(numOfPrimes)
for answer in answerList:
    print(answer)
