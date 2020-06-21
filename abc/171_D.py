"""
pypyはdictに対する処理は遅い？
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))
q = int(input())
readline = sys.stdin.readline
BC = [[int(i) for i in readline().split()] for _ in range(q)]

d = {}
for a in A:
    d[a] = d.get(a, 0) + 1

ans = []
su = sum(A)

for b,c in BC:
    if b in d:
        su = su - b*d[b] + c*d[b]
        d[c] = d.get(c, 0) + d[b]
        d.pop(b)
        ans.append(su)
    else:
        ans.append(su)

print(*ans)