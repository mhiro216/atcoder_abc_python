"""
keyword: dp, 階段登り
"""

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

MOD = 10**9+7

ok = set([i+1 for i in range(n)]) - set(a)
ok = list(ok)
ok.sort()

MAX_N = 10**5+5
dp = [0]*MAX_N

for i in ok:
    if i == 1:
        dp[i] = 1
    elif i == 2 and dp[1] == 0: # 1段目に登れなければ2段目にのぼる登り方は1通り
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = dp[i-2] + dp[i-1]
        dp[i] %= MOD
        
print(dp[n])