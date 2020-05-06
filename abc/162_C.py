"""
gcd(a,b,c) = gcd(a, gcd(b,c))
"""

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
K = int(readline())

from math import gcd

ans = 0

for i in range(1,K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            ans += gcd(i, gcd(j,k))
            
print(ans)