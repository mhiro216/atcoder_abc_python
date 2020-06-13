import sys
sys.setrecursionlimit(10**6)

n, d = map(int, input().split())

import math

tmp = d*2+1

ans = math.ceil(n/tmp)

print(ans)