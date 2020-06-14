"""
逆行列を求める
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
B = list(map(int, input().split()))

A = [[0]*n for _ in range(n)]

for i in range(n):
    if i != n-1:
        A[i][i] = 1
        A[i][i+1] = 1
    else:
        A[i][i] = 1
        A[i][0] = 1

X = [[0]*n for _ in range(n)]
for i in range(n):
    X[i][i] = 1

def Inv(A):
    """逆行列をnumpyを使わず求める"""
    
    #まずAを上三角行列にする
    for p in range(len(A)):
        pivot = A[p][p]
        for j in range(p+1, len(A)):
            coef = A[j][p] / pivot
            A[j] = [aj-ap*coef for aj,ap in zip(A[j],A[p])]
            X[j] = [xj-xp*coef for xj,xp in zip(X[j],X[p])]

    #対角成分を1にする
    for i in range(len(A)):
        X[i] = [xi/A[i][i] for xi in X[i]]
        A[i] = [ai/A[i][i] for ai in A[i]]

    #答えを出す
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            X[j] = [xj-xi*A[j][i] for xj,xi in zip(X[j],X[i])]
            A[j][i] = 0
    return X

InvA = Inv(A)

ans = [0]*n

for i in range(len(A)):
    ans[i] = int(sum([a*b for a,b in zip(InvA[i], B)])) * 2
    
print(*ans)