"""
累積GCD

左端から始めてi番目より左の数までの最大公約数をL[i], 右端から始めてi番目より右の数までの最大公約数をR[i]とする
L[i]とR[i]の最大公約数をより小さくなることがないようにi番目の数を選べるので、L[i]とR[i]の最大公約数の中で最大の値を求めれば良い
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

from math import gcd

L = [0] * n
R = [0] * n

for i in range(n-1):
    L[i+1] = gcd(L[i], A[i])
for i in range(n-1, 0, -1):
    R[i-1] = gcd(R[i], A[i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(L[i], R[i]))

print(ans)
