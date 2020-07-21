import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = input()

def pcnt(x):
    return bin(x).count('1')

def f(x):
    if x == 0: return 0
    return f(x%pcnt(x))+1

x = [0]*n

for i in range(n):
    x[i] = int(s[i])

# 元のpopcountを求める
pc = sum([x[i] for i in range(n)])

ans = [0]*n

# b(元のbit)を2通り試す
for b in range(2):
    npc = pc
    if b == 0: npc += 1
    else: npc -= 1
        
    if npc <= 0: continue # 0除算が発生するため
    
    # 元の数をpopcountで割ったあまりを求める
    # 例えば2進数1101を10進数に変換するには、1, 1の2倍の2に1を足して3, 3の2倍の6に0を足して6, 6の2倍に1を足して13、と計算できる。今回はこれを%npcする操作が加わる
    r0 = 0
    for i in range(n):
        r0 = (r0*2)%npc
        r0 += x[i]
    
    # 一番下の桁からループを回す
    # i桁目をフリップしたときのあまりを求める
    # 下からi桁目をフリップすると2^i変わる。その値をkとして計算する。同じループの中で2^i(k)のあまりも求める
    k = 1
    for i in range(n-1, -1, -1):
        if x[i] == b:
            r = r0
            # i桁目を変えたときにあまりがどう変化するか求める
            if b == 0: r = (r+k)%npc
            else: r = (r-k+npc)%npc # r-kだけだとマイナスになることがある
            ans[i] = f(r)+1
        # 2^i(k)のあまりを求める
        k = (k*2)%npc

print(*ans)