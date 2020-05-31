"""
keyword: decimal
"""
import sys
sys.setrecursionlimit(10**6)

a, b = map(str, input().split())

from decimal import *

ans = Decimal(a)*Decimal(b)
ans = int(ans)

print(ans)