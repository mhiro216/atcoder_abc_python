"""
keyword: dp

130015を13で割った時のあまりは、13001を13で割ったあまり(=1)を10倍し、5を足した数を13で割った値(=2)になる、という関係を利用する

dp[i][j] := 先頭i文字として考えられるもののうち、13で割ったあまりがjであるものの数
dp[i-1][j]、つまり先頭i-1文字目までで考えられる数で、13で割ったあまりがjであるものの数が分かっているとき、
s[i]としてとり得る値を全て試せば、dp[i][0] ~ dp[i][12]の値がわかることを利用する

例：s[i]が9なら、dp[i-1][j]を10倍し、9を足した値を13で割った値がdp[i][j]になる
"""

import sys
sys.setrecursionlimit(10**6)

s = input()

MOD = 10**9+7
dp = [[0]*13 for i in range(100005)]
n = len(s)

dp[0][0] = 1
for i in range(n):
    if s[i] == '?':
        c = -1
    else:
        c = int(s[i])
    
    for j in range(10):
        if c != -1 and c != j: continue
        for ki in range(13):
            dp[i+1][(ki*10+j)%13] += dp[i][ki]
            
    for j in range(13):
        dp[i+1][j] %= MOD
        
res = dp[n][5]

print(res)