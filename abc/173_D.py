import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))
A = [-a for a in A]

A.sort()

from heapq import *

q = A[:2][:]
heapify(q)

ans = -A[0]
q[0] = q[-1]

for a in A[2:]:
    ans += -q[0]
    tmp = heappop(q)
    tmp = max(tmp, a)
    heappush(q, tmp)
    heappush(q, a)

print(ans)