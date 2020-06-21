"""
keyword: 尺取法
"""

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
readline = sys.stdin.readline
A = [int(i) for i in readline().split()]

total = 0
right = 0
ans = 0

for i in range(n):
    while right < n and total + A[right] < k:
        total += A[right]
        right += 1
    ans += n - right
    total -= A[i]

print(ans)