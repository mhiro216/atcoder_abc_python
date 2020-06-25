"""bfs"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())

to = [[] for _ in range(n)]
cost = [[] for _ in range(n)]

for i in range(n-1):
    a,b,w = map(int, input().split())
    a -= 1; b -= 1
    to[a].append(b); cost[a].append(w)
    to[b].append(a); cost[b].append(w)

ans = [-1]*n # 頂点を探索済みかどうか判定するために初期値を-1に
ans[0] = 0

import queue

q = queue.Queue()
q.put(0)

while not q.empty():
    v = q.get()
    for i in range(len(to[v])):
        u = to[v][i]
        w = cost[v][i]
        if ans[u] != -1: continue
        ans[u] = (ans[v]+w)%2
        q.put(u)
        
print(*ans)