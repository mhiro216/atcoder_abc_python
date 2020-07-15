"""
keyword: 累積和
"""

import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
s = input()
readline = sys.stdin.readline
LR = [[int(i)-1 for i in readline().split()] for _ in range(q)] # 0-indexed

nums = [0]*(n-1)
for i in range(n-1):
    if s[i:i+2] == 'AC':
        nums[i] = 1

# 累積和を作る
tot = [0]*(len(nums)+1)
for i in range(len(nums)):
    tot[i+1] = tot[i]+nums[i]

for l,r in LR:
    print(tot[r]-tot[l])