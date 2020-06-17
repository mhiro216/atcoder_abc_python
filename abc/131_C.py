"""
keyword: 最小公倍数
"""

import sys
sys.setrecursionlimit(10**6)

a,b,c,d = map(int, input().split())

#from math import gcd
from fractions import gcd

f = gcd(c,d)
f2 = c*d//f

rem_ans = b//c - (a-1)//c + b//d - (a-1)//d - (b//f2 - (a-1)//f2) # cでもdでも割り切れる数
ans = b-a+1-rem_ans
print(ans)