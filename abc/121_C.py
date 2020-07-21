import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
readline = sys.stdin.readline
AB = [[int(i) for i in readline().split()] for _ in range(n)]

import math

AB.sort(key = lambda x: x[0])

ans = 0

while m > 0:
    for ab in AB:
        a, b = ab[0], ab[1]
        if m > b:
            ans += a*b
            m -= b
        else:
            ans += a*m
            m = 0
            
print(ans)