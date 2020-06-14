import sys
sys.setrecursionlimit(10**6)

l, r = map(int, input().split())

MOD = 2019

#n = 2019
#pf = {}
#
#for i in range(2,int(n**0.5)+1):
#    while n % i == 0:
#        pf[i] = pf.get(i,0) + 1
#        n //= i
#if n > 1: pf[n] = 1
#print(pf)
## 2019=3*673

import itertools

l_mod = l%MOD
r_mod = r%MOD

if r-l > 2019:
    ans = 0
else:
    if l_mod <= 3 <= r_mod and l_mod <= 673 <= r_mod:
        ans = 0
    elif l_mod < r_mod:
        li = [i for i in range(l_mod, r_mod+1)]
        ans = 2018
        for v in itertools.combinations(li, 2):
            ans = min(ans, v[0]*v[1]%MOD)        
    else:
        ans = 0

print(ans)