"""
誰も足止めを食わなければ5回でいける
最も多く足止めを食う場所をx回でいけるとすれば、答えは5+x-1回
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
a2e = [int(input()) for _ in range(5)]

import math

neck = min(a2e)
t_neck = math.ceil(n/neck)

ans = 5
ans += t_neck-1

print(ans)