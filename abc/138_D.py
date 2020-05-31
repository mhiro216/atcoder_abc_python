"""
keyword: dfs

PyPyだとTLE, PythonでAC
再帰関数によるDPなどを行う場合は，Pythonの方がPyPyより早い
"""
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n, q = [int(i) for i in readline().split()]
to = [[] for _ in range(n)]
ans = [0]*n

def dfs(v, p=-1): # v:これから見るnode、p:親node
    global ans
    for i in range(len(to[v])):
        u = to[v][i]
        if u == p: continue # 親nodeは確認済みなので見ない
        ans[u] += ans[v]
        dfs(u, v)

for i in range(n-1):
    a, b = [int(i) for i in readline().split()]
    a -= 1; b -= 1
    to[a].append(b)
    to[b].append(a)

for i in range(q):
    v, x = [int(i) for i in readline().split()]
    v -= 1
    ans[v] += x

dfs(0)

print(*ans)