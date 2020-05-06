"""
B=10**100
とすると、Bが非常に大きいので、B,B+1,B+2,,,B+Nの中でK個選んだ時のKが違えば、K個の値の和は必ず違う値になる
従ってKを固定した時、1,2,3,,,Nの中でK個選んだ時の総和が何通りあるかを求めれば良い

SはK以上N+1以下の値をとるものとする
総和を最小にするには、左からS個取れば良い
min L = 0+1+2+...+S-1
総和を最大にするには、右からS個取れば良い
max R = (n-S+1)+...+n
LからRの間の数は全て作れるので、Sを固定したときに取り得る値はR-L+1通りある

左端l、右端rの公差1の等差数列の和は
(l+r)*(r-l+1)/2
"""

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
N,K = [int(i) for i in readline().split()]

ans = 0

def sum(l, r):
    return (l+r)*(r-l+1)//2

for S in range(K, N+2):
    L = sum(0, S-1)
    R = sum(N-S+1, N)
    ans += (R-L+1)%(10**9+7)

ans %= 10**9+7
print(ans)