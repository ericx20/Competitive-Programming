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

num = int(input())
for i in range(num, 999999999999999):
    if checkPrime(i):
        #print("Next prime:")
        print(i)
        break
