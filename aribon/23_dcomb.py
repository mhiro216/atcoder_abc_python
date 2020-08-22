# 重複組み合わせ
# 解説　https://emtubasa.hateblo.jp/entry/2018/08/29/161456

n = 3
m = 3
a = [1, 2, 3]
M = 10000

dp = [[0]*(m+1) for i in range(n+1)]

# dp[i+1][j] := i番目までの品物からj個選ぶ組み合わせの総数

# 1つも選ばない方法は常に１通り
for i in range(n+1):
    dp[i][0] = 1

for i in range(n):
    for j in range(1, m+1):
        if j - 1 - a[i] >= 0:
            # 引き算が含まれる場合は負の数にならないように注意する
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j] - dp[i][j-1-a[i]] + M) % M
        else:
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % M

print(dp[n][m])
