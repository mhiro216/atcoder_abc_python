"""最小公倍数"""
a, b = map(int, input().split())

#from math import gcd
from fractions import gcd

f = gcd(a,b)
f2 = a*b//f

print(f2)