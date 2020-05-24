"""
keyword: 二分探索

初めにLをソートして、a<b<cとしてa,bを決めたとき、a+b>cとなるようなcの個数を計算する
cの最大値を求めるには二分探索が高速
さらに、二分探索の探索範囲の左端は、前のループで求めたcの最大値で十分である（∵前のループのa+b <= 今ループのa+b）ことを考慮すれば、さらに高速化できる

pythonでTLE, pypyでAC
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0

for i in range(n-2):
    l_prev = 0 # 前のループで求めたcの最大値を覚えておく
    for j in range(i+1,n-1):
        ab = L[i]+L[j]
        if not l_prev:
            l = j; r = n
        else:
            l = l_prev; r = n
        while l+1 < r:
            c = (l+r)//2
            if L[c] < ab:
                l = c
            else:
                r = c
        ans += l-j
        l_prev = l
        
print(ans)