import sys
input = sys.stdin.readline
h = int(input())
for i in range(h // 2):
    print("*" * (i * 2 + 1) + " " * (2 * h - i * 4 - 2) + "*" * (i * 2 + 1))
print("*" * (h * 2))
for i in reversed(range(h // 2)):
    print("*" * (i * 2 + 1) + " " * (2 * h - i * 4 - 2) + "*" * (i * 2 + 1))
