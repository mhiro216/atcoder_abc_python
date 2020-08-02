import sys
sys.setrecursionlimit(10**6)

n, d = map(int, input().split())
readline = sys.stdin.readline
xy = [[int(i) for i in readline().split()] for _ in range(n)]

import math

ans = 0

for x,y in xy:
    dist = math.sqrt(pow(x,2) + pow(y,2))
    if dist <= d:
        ans += 1

print(ans)