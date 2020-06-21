"""
keyword: 辞書順
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())

sp = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    sp.append([s,p, i+1])

sp.sort(key=lambda x: x[1], reverse=True)
sp.sort(key=lambda x: x[0])

ans = [i[2] for i in sp]

print(*ans)