## DFS Lake Counting

N = 10
M = 12
field = [
    'W........WW.',
    '.WWW.....WWW',
    '....WW...WW.',
    '.........WW.',
    '.........W..',
    '..W......W..',
    '.W.W.....WW.',
    'W.W.W.....W.',
    '.W.W......W.',
    '..W.......W.'
]
#field = [
#    'W...........',
#    '............',
#    '..W.........',
#    '............',
#    '....W.......',
#    '............',
#    '......W.....',
#    '............',
#    '............',
#    '............'
#]

field = [list(f) for f in field]

def dfs(x, y):
    # 今いるところを'.'に置き換える
    field[x][y] = '.'
    
    # 移動する8方向をループ
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # x方向にdx, y方向にdy移動した場所を(nx, ny)とする
            nx = x + dx; ny = y + dy
            
            # nxとnyが庭の範囲内かどうかとfield[nx][ny]が水たまりかどうかを判定
            if 0 <= nx and nx < N and 0 <= ny and ny < M and field[nx][ny] == 'W':
                dfs(nx, ny)
    
    return

def lake_counting():
    res = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'W':
                # 'W'が残っているならそこからdfsを始める
                dfs(i, j)
                res += 1
                
    return res

print(lake_counting())