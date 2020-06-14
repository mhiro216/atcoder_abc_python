import sys
sys.setrecursionlimit(10**6)

n, d = map(int, input().split())
readline = sys.stdin.readline
x = [[int(i) for i in readline().split()] for _ in range(n)]

import itertools
import math

ans = 0

for v in itertools.combinations(x, 2):
    dist = math.sqrt(sum([(i-j)**2 for i,j in zip(v[0], v[1])]))
    if dist == int(dist):
        ans += 1
        
print(ans)