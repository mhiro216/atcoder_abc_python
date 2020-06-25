"""
初めのサイコロの目がiのとき、2のt乗が初めてk以上となるような整数tを求める

i*2**t >= k
2**t >= k/i
tlog(2) >= log(k/i)
t >= log(k/i)/log(2)
"""

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

import math

ans = 0

for i in range(1,n+1):
    if i >= k:
        t = 0
    else:
        t = math.ceil(math.log(k/i)/math.log(2))
    ans += 1/math.pow(2, t)

ans /= n

print(ans)