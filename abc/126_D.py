"""dfs"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
 
G = {}
for i in range(n):
    G.update({i:[]})

for i in range(n-1):
    u,v,w = map(int, input().split())
    u -= 1; v -= 1
    G[u].append([v, w%2])
    G[v].append([u, w%2])

color = [-1 for i in range(n)]

def dfs(graph, v, c):
    color[v] = c
    
    for next_v in graph[v]:
        if color[next_v[0]] != -1: continue
        dist = next_v[1]
        if dist == 0:
            next_c = c
        elif dist == 1:
            next_c = 1 - c
        
        dfs(graph, next_v[0], next_c)

dfs(G, 0, 0)

print(*color)