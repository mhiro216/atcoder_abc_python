"""
逆順に見ていけばボールの入れ方は一意に決まっていくことに注意

例：N=6でa6=1なら6番目の箱にはボールを入れなくてはならない、a5=1なら5番目の箱にはボールを入れなくてはならない、、、2番目の箱にボールを入れるかどうかは倍数である4, 6番目の箱を見て決める
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = [0]
a += list(map(int, input().split()))

b = [0]*(n+1)

for i in range(n,0,-1):
    sum = 0
    for j in range(2*i, n+1, i):
        sum ^= b[j] # XOR
    b[i] = sum^a[i]
    
ans = []
for i in range(1,n+1):
    if b[i]: ans.append(i)

print(len(ans))
print(*ans)