"""
keyword: ダイクストラ
"""
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n,m,s = [int(i) for i in readline().split()]
g = [[] for _ in range(n)]
for i in range(m):
    u,v,a,b = [int(i) for i in readline().split()]
    u -= 1
    v -= 1
    g[u].append((v,a,b)) # (つながっている頂点、かかる金額、かかる時間)
    g[v].append((u,a,b))


cd = [int(i) for i in read().split()]
c = cd[::2]
d = cd[1::2]


from heapq import *
INF = 1e18
M = 2500 # 無駄なことをしなければ、移動する辺の数は高々N-1。従って必要なお金は高々50*50
if s >= M: s = M-1
dist = [[INF]*M for _ in range(n)] # startからの最短時間。頂点(高々50)×所持金(高々2500)の状態を持っておく
dist[0][s] = 0
q = [(0,s,0)] # (そこまでの時間、所持金、頂点)。頂点v、所持金sの状態に時間xで行ける、と言う意味

while q:
    dv, num, v = heappop(q)
    
    if dist[v][num] <= dv: continue
        
    if num+c[v] < M and dv+d[v] < dist[v][num+c[v]]:
        dist[v][num+c[v]] = dv + d[v]
        heappush(q, (dv+d[v], num+c[v], v))
        
    for to,a,b in g[v]:
        if num >= a and dv + b < dist[to][num-a]:
            dist[to][num-a] = dv + b
            heappush(q, (dv+b, num-a, to))

for i in range(1,n):
    print(min(dist[i]))