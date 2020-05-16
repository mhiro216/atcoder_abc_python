"""
有向グラフ, ビット演算

`for i in range(1<<n)`の意味
n人の人が正直かどうかで2**n通り試す必要がある。1<<n=2**n
ここで、iが何を表すことにしているか。
例えばi=10だったら、二進数で表すと001010となるが、j番目の人が正直かどうかをj桁目が1かどうかで表していることにする。つまりここでは1,3番目の人が正直者で、0,2,4,5番目の人がそうではないことを表している。
"""

n = int(input())

g = [[0]*15 for i in range(15)]

for i in range(n):
    for j in range(n):
        g[i][j] = -1 # i番目の人がj番目の人を何と言っているか。何も証言されていない状態を-1。入力(1or0)があればその値を代入
for i in range(n):
    m = int(input())
    for j in range(m):
        a, x = map(int, input().split())
        a -= 1
        g[i][a] = x

ans = 0
for i in range(1<<n):
    d = [0]*n
    for j in range(n):
        if i>>j&1: # iのj桁目が1か
            d[j] = 1
    ok = True
    for j in range(n):
        if d[j]: # 正直な人の証言だけに注目すれば良い
            for k in range(n):
                if g[j][k] == -1: continue
                if g[j][k] != d[k]: ok = False
    if ok: ans = max(ans, bin(i).count('1'))

print(ans)