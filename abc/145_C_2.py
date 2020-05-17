"""
n!通りの中で、各辺が何回使われるかに注目する
各辺が使われる回数は、全ての辺で明らかに同じことを利用する
各辺が使われる回数をxとすると、n!通りの移動で使われる辺の数の合計は
辺の本数*x
とも表せるし
(n-1)*n! ※全頂点を回るのにn-1個の辺を使うため
とも表せる

辺の本数はnC2なので
nC2*x = (n-1)*n!
となる。これを利用してxを求めると
x = 2*(n-1)!
となる

求めたいものはn!通りの移動距離の平均。よって
（辺の長さの合計）* x / n!
を求めれば良い
"""

n = int(input())

x = []; y = []
for i in range(n):
    i,j = map(int, input().split())
    x.append(i)
    y.append(j)

import math

def dist(i,j):
    dx = x[i]-x[j]
    dy = y[i]-y[j]
    return math.sqrt(dx*dx+dy*dy)

from itertools import combinations

node = [i for i in range(n)]
node_combs = list(combinations(node,2))

sum_dist = 0
for node_comb in node_combs:
    sum_dist += dist(node_comb[0], node_comb[1])

ans = sum_dist * 2 / n

print(ans)