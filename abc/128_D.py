"""
左からとった個数と右からとった個数の合計がmin(n, k)となることに注意して、全てのパターンについて試す
操作できる残り回数を算出して、マイナスを取り除くために使う
"""

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
v = list(map(int, input().split()))

vr = v[::-1]

ans = 0

mi = min(n,k)

for i in range(mi+1):
    for j in range(mi-i+1):
        minus = 0 # 後で取り除くマイナスの値の合計
        now = v[:i]+vr[:j]
        d = k-(len(now)) # 操作できる残り回数。マイナスを取り除いて合計値を上げるために行う
        now.sort()
        md = min(d, len(now))
        for s in range(md):
            if 0 <= now[s]:
                break
            minus += now[s]
    ans = max(ans, sum(now)-minus)

print(ans)