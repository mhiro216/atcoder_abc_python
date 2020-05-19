"""bfs"""
import sys
sys.setrecursionlimit(10**6)
n,m = map(int, input().split())

INF = 1001001001

to = [[] for _ in range(n)]
dist = [INF]*n
dist[0] = 0
ans = [-1]*n
ans[0] = [0]

for i in range(m):
    a,b = map(int, input().split())
    a -= 1; b -= 1
    to[a].append(b)
    to[b].append(a)

import queue

q = queue.Queue()
q.put(0)

while not q.empty():
    v = q.get()
    for i in range(len(to[v])):
        u = to[v][i]
        if dist[u] != INF: continue # 更新済みならこの後の処理を行わない
        dist[u] = dist[v]+1
        ans[u] = v
        q.put(u)

if -1 not in ans:
    print('Yes')
    for i in ans[1:]: print(i+1)
else:
    print('No')