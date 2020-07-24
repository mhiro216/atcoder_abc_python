## BFS 迷路の最短路

N = 10
M = 10
field = [
    '#S######.#',
    '......#..#',
    '.#.##.##.#',
    '.#........',
    '##.##.####',
    '....#....#',
    '.#######.#',
    '....#.....',
    '.####.###.',
    '....#...G#'
]

field = [list(f) for f in field] # 迷路を表す配列
sx, sy = 0, 1 # スタートの座標
gx, gy = 9, 8 # ゴールの座標

INF = 10**8
d = [[0]*M for i in range(N)] # 各点までの最短距離の配列
dx = [1,0,-1,0]; dy = [0,1,0,-1] # 移動4方向のベクトル

# (sx, sy)から(gx, gy)への最短距離を求める
# たどり着けないとINF
import queue

def bfs():
    que = queue.Queue()
    # 全ての点をINFで初期化
    for i in range(N):
        for j in range(M):
            d[i][j] = INF
    # スタート地点をキューに入れ、その点の距離を0にする
    que.put([sx, sy])
    d[sx][sy] = 0
    
    # キューが空になるまでループ
    while que.qsize():
        # キューの先頭を取り出す
        p = que.get()
        # 取り出してきた状態がゴールなら探索を辞める
        if p[0] == gx and p[1] == gy: break
        
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を(nx, ny)とする
            nx = p[0] + dx[i]; ny = p[1] + dy[i]

            # 移動が可能かの判定と既に訪れたことがあるかの判定(d[nx][ny] != INF なら訪れたことあり)
            if 0 <= nx and nx < N and 0 <= ny and ny < M and field[nx][ny] != '#' and d[nx][ny] == INF:
                # 移動できるならキューに入れ、その点の距離をpからの距離+1で確定する
                que.put([nx, ny])
                d[nx][ny] = d[p[0]][p[1]] + 1
            
    return d[gx][gy]

def meiro():
    res = bfs()
    return res

print(meiro())