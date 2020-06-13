"""
keyword: heap
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
readline = sys.stdin.readline
A = [int(input()) for _ in range(n)]

import heapq

Q = [-a for a in A]
heapq.heapify(Q)

ans = []

for i in range(n):
    if -Q[0] == A[i]:
        tmp = heapq.heappop(Q)
        ans.append(-Q[0])
        heapq.heappush(Q, tmp)
    else:
        ans.append(-Q[0])

print(*ans)