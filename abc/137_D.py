"""
keyword: heap
"""
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

from heapq import *

n,m = [int(i) for i in readline().split()]
ab = [[int(i) for i in readline().split()] for _ in range(n)]

ab.sort(reverse = True)

q = []
ans = 0
for i in range(m-1,-1,-1):
    while ab and ab[-1][0] + i <= m:
        (a,b) = ab.pop()
        heappush(q,-b)
    
    if q: ans -= heappop(q)

print(ans)
