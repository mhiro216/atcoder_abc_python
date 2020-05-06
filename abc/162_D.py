"""
j−i != k−j
の条件がなければ、Rの数*Gの数*Bの数(*1)が答え

そこでまず*1を求めて、次に
j-i == k-j
となるような場合の数を求め、*1から引いたものが答え
"""

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = int(readline())
s = readline()

a = [0]*n
for i in range(n):
    if s[i] == 'R': a[i] = 0
    if s[i] == 'G': a[i] = 1
    if s[i] == 'B': a[i] = 2

cnt = [0]*3
for i in range(n):
    cnt[a[i]] += 1
    
ans = 1
for i in range(3):
    ans *= cnt[i]

for j in range(n):
    for i in range(j):
        k = j + (j-i)
        if k < n:
            if a[i] == a[j]: continue
            if a[i] == a[k]: continue
            if a[k] == a[j]: continue
            ans -= 1

print(ans)