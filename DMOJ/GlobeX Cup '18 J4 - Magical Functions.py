import sys
from functools import lru_cache

a, b, c, d, e, N = [int(num) for num in sys.stdin.readline().split()]
@lru_cache(maxsize=None)
def f(x):
    if x == 0:
        return e
    else:
        return a*f(int(x/b)) + c*f(int(x/d))
print(f(N) % (10**9 + 7))
