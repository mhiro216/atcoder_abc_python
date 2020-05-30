"""
keyword: dfs
"""

import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
to = [[] for _ in range(n)]
ans = [0]*n

def dfs(v, p=-1): # v:これから見るnode、p:親node
    global ans
    ans[v] += ans[p]
    for i in range(len(to[v])):
        u = to[v][i]
        if u == p: continue # 親nodeは確認済みなので見ない
        dfs(u, v)

for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1; b -= 1
    to[a].append(b)
    to[b].append(a)

for i in range(q):
    v,x = map(int, input().split())
    v -= 1
    ans[v] += x

dfs(0)

print(*ans)