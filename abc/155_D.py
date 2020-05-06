"""
k番目の値をxとしたとき、「x未満の値がk個未満」であるxの最大値を求める（k-1個と言い切っていないのは、同じ数が並ぶことがあるため）
x未満であることをOKと呼ぶと、値がソート済みの状態なら左からOKが並び右からNGが並んでいる状態。ここでOKとNGの境界線を求める問題になる。二分探索で解く

「x未満の値が何個できるか」をどう数えるか
整数のペアのうち一方の値を固定したとき、もう片方の値をどこまで大きくできるかは、値がソート済みの状態なら左から何個まで取り得るか、になる。これも二分探索で解く
自分自身同士のペアは数えないし、自分と相手をひっくり返したペアも2度は数えないが、一旦無視してカウントし、最後に調整する
ただし、一方の値が負のときは、左から何個まで取り得るかではなく、右から何個まで取り得るかになる点に注意
"""

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,k = [int(i) for i in readline().split()]
a = [int(i) for i in readline().split()]

INF = 10**18+5

a.sort()

def is_ok(x):
    tot = 0 # x未満のペアの数
    for i in range(n):
        if a[i] < 0:
            l = -1; r = n # lがng, rがok側. 
            while l+1 < r:
                c = (l+r)//2
                if a[c]*a[i] < x:
                    r = c # ここだけa[i]>0の場合と変わる
                else:
                    l = c # ここだけa[i]>0の場合と変わる
            tot += n-r
        else:
            l = -1; r = n # lがok, rがng側. okが1つもないならlが-1に、全てokならlがn-1になるように初期値を定める
            while l+1 < r:
                c = (l+r)//2
                if a[c]*a[i] < x:
                    l = c
                else:
                    r = c
            tot += r
        if a[i]*a[i] < x: tot -= 1 # 自分自身をペアにとっているものでカウントされているものは引いておく
    tot //= 2 # (1,2)と(2,1)を別のものとして数えているので2で割る
    return tot < k

l = -INF; r = INF
while l+1 < r: # lとrが隣り合ったら終わり
    x = (l+r)//2
    if is_ok(x):
        l = x
    else:
        r = x
        
print(l)