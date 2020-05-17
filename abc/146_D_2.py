"""bfs"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())

to = [[] for _ in range(n)]
eid = [[] for _ in range(n)]
ans = [0]*(n-1)

for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1; b -= 1
    to[a].append(b); eid[a].append(i) # to:nodeの繋がり、eid:edgeの色
    to[b].append(a); eid[b].append(i)

import queue

q = queue.Queue()
used = [0]*n
q.put(0)
used[0] = 1 # qに突っ込んだ時点でその頂点のusedを1にする

while not q.empty():
    v = q.get()
    c = -1
    for i in range(len(to[v])):
        u = to[v][i]; ei = eid[v][i]
        if used[u]: c = ans[ei]
    k = 1
    for i in range(len(to[v])):
        u = to[v][i]; ei = eid[v][i]
        if used[u]: continue
        if k == c: k += 1
        ans[ei] = k
        k += 1
        q.put(u)
        used[u] = 1 # qに突っ込んだ時点でその頂点のusedを1にする

mx = 0
for i in range(n):
    mx = max(mx, len(to[i]))
print(mx)
for i in range(n-1):
    print(ans[i])