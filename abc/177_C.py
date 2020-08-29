import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

MOD = 10**9+7

tot = sum(A)
tot %= MOD

ans = 0
rmv = 0

for a in A:
    rmv += a
    rmv %= MOD
    ans += a*(tot-rmv)
    ans %= MOD

print(ans)
