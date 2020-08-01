# 最長増加部分列

"""
dp[i] := 最後がaiであるような最長の増加部分列の長さ

最後がaiであるような増加部分列は
 aiのみから成る列
 j<iかつaj<aiであるようなajで終わる増加部分列の後ろにaiを付け足した列
のどちらか

dp[i] = max{1, dp[j]+1 | j<i かつ aj<ai}
"""

n = 5
a = [4,2,3,1,5]

dp = [0]*n

res = 0
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)
    res = max(res, dp[i])

print(res)

"""
別解
https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
"""

import bisect

res = [a[0]]
for i in range(len(a)):
    if a[i] > res[-1]:
        res.append(a[i])
    else:
        res[bisect.bisect_left(res, a[i])] = a[i] # bisect.bisect_left(res, a[i])は、resの中にa[i]を入れる場合にa[i]が入るべきインデックスを返す

print(len(res))