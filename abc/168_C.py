"""余弦定理"""
import sys
sys.setrecursionlimit(10**6)
a,b,h,m = map(int, input().split())

import math

h_rad = 30*(h+m/60)
m_rad = 6*m
diff_rad = min(abs(h_rad-m_rad),360-abs(h_rad-m_rad))
cos = math.cos(math.radians(diff_rad))

ans = math.sqrt(a*a+b*b-2*a*b*cos)
print(ans)