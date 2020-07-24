## 最長共通部分列

n = 4
m = 4
s = "abcd"
t = "becd"

dp = [[0]*(m+1) for i in range(n+1)]

def lcs():
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[n][m]

print(lcs())