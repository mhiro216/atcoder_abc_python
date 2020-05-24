"""
keyword: 最大公約数, 素因数分解

最大公約数を素因数分解し、素因数の集合の個数+1(∵1は素数ではないが答えには入る)を数えれば良い
"""

a,b = map(int, input().split())

#from math import gcd
from fractions import gcd

g = gcd(a,b)

pf = {}

for i in range(2,int(g**0.5)+1):
    while g % i == 0:
        pf[i] = pf.get(i,0) + 1
        g //= i
if g > 1: pf[g] = 1

ans = 1 + len(pf.keys()) # 1は素数ではないが答えには入る

print(ans)