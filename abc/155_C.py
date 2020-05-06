import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = int(readline())
s = [readline().rstrip() for _ in range(n)]

import collections

c = collections.Counter(s)
c = c.most_common()

ans = [c[0][0]]
v_max = c[0][1]
for k,v in c[1:]:
    if v == v_max:
        ans.append(k)
ans.sort()

for a in ans:
    print(a)