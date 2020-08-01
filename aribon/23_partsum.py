# 個数制限付き部分和

"""
dp[i+1][j]:=i番目まででjを作る際に余る最大のi番目の個数（作れない場合は-1）

i-1番目まででjを作れる(dp[i][j]>=0)なら、aiをmi個残してjを作れる
i番目まででj-aiを作る際にaiをk(>0)個残せるなら、aiをもう1つ足せばjが作れる。すなわちaiをk-1個残してjを作れる

dp[i+1][j] = {
    mi (dp[i][j]>=0)
    -1 (j<aiまたはdp[i+1][j-ai]<=0)
    dp[i+1][j-ai]-1 (それ以外)
    }

最終的な答えはdp[n][K]>=0であるかを調べることで得られる
"""

n = 3
a = [3,5,8]
m = [3,2,2]
K = 17

MAX_K = 10**5

dp = [-1]*(MAX_K+1)

dp[0] = 0

for i in range(n):
    for j in range(K+1):
        if dp[j] >= 0:
            dp[j] = m[i]
        elif j < a[i] or dp[j-a[i]] <= 0:
            dp[j] = -1
        else:
            dp[j] = dp[j-a[i]] - 1

if dp[K] >= 0: print('Yes')
else: print('No')