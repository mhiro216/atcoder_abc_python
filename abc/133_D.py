"""
ある1点の値をxと決めると、各頂点の値をxを使って表せる
A1-x, A2-A1+x, A3-A2+A1-x,,,
1周回ると、
x = A5-A4+A3-A2+A1-x
などと表せる
これを使ってxを求め、各頂点の値を計算していけば良い
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

x2 = 0
for i in range(n):
    if i%2:
        x2 -= a[i]
    else:
        x2 += a[i]

ans = [0]*n
ans[0] = x2//2

for i in range(n-1):
    ans[i+1] = a[i] - ans[i]
    
for i in range(n):
    ans[i] *= 2
    
print(*ans)