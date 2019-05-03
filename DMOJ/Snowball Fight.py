# h is the number of snowballs it takes to make the person give up
# w is the cooldown time in seconds for a person to throw again
h1, w1 = [int(x) for x in input().split()]
h2, w2 = [int(x) for x in input().split()]
# start at 1 because at t=0 into the game, they both throw
numHits1 = 1
numHits2 = 1


# time left to hit again
cooldown1 = w1
cooldown2 = w2

time = 0
while True:
    time += 1
    if (numHits1 == h1) and (numHits2 == h2):
        print("-1")
        break
    elif numHits1 == h1:
        print("2")
        break
    elif numHits2 == h2:
        print("1")
        break
    cooldown1 += -1
    cooldown2 += -1
    # P1 hits P2
    if cooldown1 == 0:
        numHits2 += 1
        cooldown1 = w1

    # P2 hits P1
    if cooldown2 == 0:
        numHits1 += 1
        cooldown2 = w2
