n,x,y = list(map(int, input().split()))

INF = 1001001001

from collections import deque

def push(v,d):
    if dist[v] != INF:
        return
    dist[v] = d
    q.append(v)

x -= 1
y -= 1
ans = [0] * n

for sv in range(n):
    dist = [INF] * n
    q = deque()
    push(sv, 0)
    while len(q):
        v = q.popleft()
        d = dist[v]
        if v-1 >= 0: push(v-1, d+1)
        if v+1 < n: push(v+1, d+1)
        if v == x: push(y, d+1)
        if v == y: push(x, d+1)
    for i in range(n):
        ans[dist[i]] += 1

for i in range(n):
    ans[i] //= 2 # (1,2)と(2,1)を2度数えてしまっているので2で割る

for i in range(1,n):
    print(ans[i])