## 01ナップサック問題

n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

# i番目以降の品物から重さの総和がj以下となるように選ぶ
def rec(i, j):
    if i == n:
        res = 0
    elif j < w[i]:
        # この品物は入らないのでi+1番目以降の品物の検討に移る
        res = rec(i+1, j)
    else:
        # 入れない場合と入れる場合を両方試す。品物を入れると価値はv[i], 許容できる残りの重さはj-w[i]となる
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    
    return res

def knapsack():
    return rec(0, W)

print(knapsack())

## 01ナップサック問題　メモ化

dp = [[-1]*(W+1) for i in range(n+1)]

def rec(i, j):
    if dp[i][j] >= 0:
        # すでに調べたことがあるならその結果を再利用
        return dp[i][j]
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i+1, j)
    else:
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    # 結果をテーブルに記憶する
    dp[i][j] = res
    return res
        
def fast_knapsack():
    return rec(0, W)

print(fast_knapsack())

## 個数制限なしナップサック問題

"""
dp[i+1][j]を、i番目までの品物から重さの総和がj以下となるように選んだときの、価値の総和の最大値とする

漸化式は、
dp[0][j] = 0
dp[i+1][j] = max{dp[i][j-k*w[i]] + k*v[i] | 0<=k}

このとき、dp[i+1][j]の計算においてk(>=1)個選ぶ場合は、dp[i+1][j-w[i]]の計算においてk-1個選んだ場合と同様。(※1)

  max{dp[i][j-k*w[i]] + k*v[i] | 0<=k}
= max(dp[i][j], max{dp[i][j-k*w[i]] + k*v[i] | 1 <= k})
= max(dp[i][j], max{dp[i][(j-w[i])-k*w[i]] + k*v[i] | 0 <= k} + v[i]) # ※1を利用して式変換
= max(dp[i][j], dp[i+1][j-w[i]] + v[i]) # 漸化式の2式目を利用して式変換
"""

n = 3
w = [3,4,2]
v = [4,5,3]
W = 7

dp = [[0]*(W+1) for i in range(n+1)]

def nolimit_knapsack():
    for i in range(n):
        for j in range(W+1):
            if j < w[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-w[i]] + v[i])
    return dp[n][W]

print(nolimit_knapsack())

## 01ナップサック問題　漸化式

dp = [[0]*(W+1) for i in range(n+1)]

def fast_knapsack():
    for i in range(n-1, -1, -1):
        for j in range(W+1):
            if j < w[i]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-w[i]]+v[i])
    return dp[0][W]

print(fast_knapsack())

## 01ナップサック問題　再び

n = 4
w = [2,1,3,2]
v = [3,2,4,2]
W = 5

dp = [0 for i in range(W+1)]

def knapsack():
    for i in range(n):
        for j in range(W, w[i]-1, -1):
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
    return dp[W]

print(knapsack())

## 個数制限なしナップサック問題　再び

n = 3
w = [3,4,2]
v = [4,5,3]
W = 7

dp = [0 for i in range(W+1)]

def nolimit_knapsack():
    for i in range(n):
        for j in range(w[i], W+1):
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
    return dp[W]

print(nolimit_knapsack())