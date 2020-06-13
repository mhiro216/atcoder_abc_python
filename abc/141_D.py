"""
keyword: heap

最大値を取り出して2で割って戻し、その時点の最大値を取り出して2で割って戻し、、、を繰り返す
heapを使う。heapは最小値しか取り出せないので、マイナスをかけて最大値を取り出せるようにする
"""

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
A = list(map(int, input().split()))

import heapq

A = [-a for a in A]
heapq.heapify(A)

for _ in range(m):
    tmp = heapq.heappop(A)/2
    heapq.heappush(A, tmp)
    
ans = 0
for a in A:
    ans += -int(a)
print(ans)