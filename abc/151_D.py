"""
bfsの問題
蟻本p37参考
"""

h, w = list(map(int, input().split()))
s = [input() for _ in range(h)]

INF = 1001001001
di = [-1,0,1,0]
dj = [0,-1,0,1]
ans = 0

def update(i, j, x):
    if dist[i][j] != INF: return
    dist[i][j] = x
    que.put([i,j])

import queue

# スタートの座標全てのパターンについて距離を計算
for si in range(h):
    for sj in range(w):
        if s[si][sj] == '#': continue
        dist = [[INF]*w for i in range(h)]
        que = queue.Queue()
        update(si, sj, 0)
        while que.qsize():
            p = que.get()
            i = p[0]; j = p[1]
            for drc in range(4):
                ni = i+di[drc]; nj = j+dj[drc]
                if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
                if s[ni][nj] == '#': continue
                update(ni, nj, dist[i][j]+1)
        # ゴールの座標全てのパターンについて距離を更新
        for i in range(h):
            for j in range(w):
                if dist[i][j] == INF: continue
                ans = max(ans, dist[i][j])

print(ans)