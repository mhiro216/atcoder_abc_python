# https://img.atcoder.jp/abc172/editorial.pdf

import sys
sys.setrecursionlimit(10**6)

N = int(input())

ans = 0

for i in range(1, N+1):
    n = N//i
    tot = i*(1+n)*n//2
    ans += tot
    
print(ans)