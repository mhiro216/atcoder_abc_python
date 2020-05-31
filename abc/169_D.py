"""
keyword: 素因数分解、二分探索

まずは素因数分解
素因数分解の結果、例えば素数2が5個現れる場合、異なるzで割る際は、2, 2*2, 2*2*2の3つのzで割るのが、最大で行える操作の回数
つまり、各素数について、最大で行える操作の回数mは、1からmまでの公差1の等差数列の和 m*(m+1)/2 が素数の数以下であるような最大の値
このようなmの値は、二分探索で求まる
"""
import sys
sys.setrecursionlimit(10**6)

n = int(input())

pf = {}

for i in range(2,int(n**0.5)+1):
    while n % i == 0:
        pf[i] = pf.get(i,0) + 1
        n //= i
if n > 1: pf[n] = 1

ans = 0

for v in pf.values():
    
    l = 1; r = v

    while l+1 < r:
        c = (l+r)//2
        if c*(c+1)/2 <= v:
            l = c
        else:
            r = c
    ans += l

print(ans)