def isPink(r, g, b):
    if 240 <= r <= 255:
        if 0 <= g <= 200:
            if 95 <= b <= 220:
                return True
    return False
n = int(input())
numPink = 0
for i in range(n):
    x, y, z = [int(x) for x in input().split()]
    if isPink(x, y, z):
        numPink += 1
print(numPink)
