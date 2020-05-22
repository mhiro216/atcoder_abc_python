"""
AiAj+BiBj=0
Bi, Ajが0でなければ
Ai/Bi=-Bj/Aj
Ai/Bi=Xiとすると
Xi=-1/Xj
Xj=-1/Xi

一緒に選んではいけない数はグループ化できて、Sグループに所属する数はTグループに所属する数と一緒に選べない、という関係になる
この場合の数の選び方は

- Sからのみ1匹以上選ぶ 2**S-1通り（各々を選ぶかどうかで2通りずつ。最後に全員を選ばない1通りを引く）
- Tからのみ1匹以上選ぶ 2**T-1通り
- どちらからも選ばない 1通り

この場合の数の和をRとすると、(Sx,Tx)から選ぶ場合の数をRx通りとすると
R1*R2*R3...
通りとなる

ただしこれではAi,Biが0の場合を考慮できていない
そこで、まずgcdを使って比ををとる操作をする

gcd(Ai,Bi)=gi
Ai'=Ai/gi
Bi'=Bi/gi

この操作により、(3,5)と(9,15)が同じ値になってグループ分けがしやすくなる
後は、(-3,5)と(3,-5)が同じになるようにしたい。Ai>=0の制限をかけて、そうでなければマイナスを移すようにすると、いずれも(3,-5)になる
後はいずれかが0のとき。(0,5)のときは(0,1),(3,0)のときは(1,0)にする

(0,0)のケースだけ例外。常にAiAj+BiBj=0なので、誰と組んでも仲が悪くなる。つまり(0,0)のグループがある
ただし他を選ばず(0,0)だけを選ぶのは許容されている。したがって(0,0)の数zだけ数えておいて、最後にz通りを足せば良い。

さらに全体から1人は最低でも選ばなければいけないことを考慮して、答えは

R1*R2*R3...-1+z通り

となる
"""
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = int(input())
ab = [[int(i) for i in readline().split()] for _ in range(n)]

d = {}
zero = 0

from math import gcd

for a,b in ab:
    if a == b == 0:
        zero += 1
        continue
    g = gcd(a,b)
    a //= g
    b //= g
    # bが必ず正になるように値を変換
    if b < 0:
        a = -a
        b = -b
    if b == 0 and a == -1:
        a = 1
    
    if a > 0:
        if (a,b) in d:
            d[(a,b)][0] += 1
        else:
            d[(a,b)] = [1,0]
    else:
        if (b,-a) in d:
            d[(b,-a)][1] += 1
        else:
            d[(b,-a)] = [0,1]

MOD = 10**9+7
ans = 1

pow2 = [1]
for _ in range(200005):
    pow2.append(pow2[-1]*2%MOD)

for (a,b),(k,l) in d.items():
    ans *= pow2[k]+pow2[l]-1
    ans %= MOD

ans += zero-1
print(ans%MOD)