questionType = int(input())
n = int(input())
country1 = [int(x) for x in input().split()]
country2 = [int(x) for x in input().split()]

country1.sort()
country2.sort()
total = 0

if questionType == 1:
    for i in range(n):
        total += max(country1[i], country2[i])
else:
    for i in range(n):
        total += max(country1[i], country2[n-i-1])
print(total)
