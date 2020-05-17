"""dfs"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())

to = [[] for _ in range(n)]
eid = [[] for _ in range(n)]
ans = [0]*(n-1)

def dfs(v, c=-1, p=-1): # v:これから見るnode、c:pとvを繋ぐedgeの色、p:親node
    k = 1
    for i in range(len(to[v])):
        u = to[v][i]
        ei = eid[v][i]
        if u == p: continue # 親nodeは確認済みなので見ない
        if k == c: k += 1 # 親nodeとの間のedgeの色と同じではいけないのでインクリメントする
        ans[ei] = k
        k += 1
        dfs(u,ans[ei],v)

for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1; b -= 1
    to[a].append(b); eid[a].append(i) # to:nodeの繋がり、eid:edgeの色
    to[b].append(a); eid[b].append(i)

dfs(0)

mx = 0
for i in range(n):
    mx = max(mx, len(to[i]))
print(mx)
for i in range(n-1):
    print(ans[i])