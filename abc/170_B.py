"""
a+b=x <=> 2*a+2*b=2*x
2*a+4*b=y
"""

import sys
sys.setrecursionlimit(10**6)

x, y = map(int, input().split())

b = y/2-x
a = 2*x-y/2

if b >= 0 and b == int(b) and a >= 0 and a == int(a):
    print('Yes')
else:
    print('No')