"""
Point: 割り切れるかどうかの情報を配列で持っておく
"""

N = int(input())
A = [int(i) for i in input().split()]

D = set()
S = set()
for i in range(N):
    if A[i] in S:
        D.add(A[i])
    else:
        S.add(A[i])

M = max(S)

X = [1 for i in range(M+1)] # 割り切れない場合1
for a in S:
    if a in D:
        X[a] = 0
    for i in range(2*a, M+1, a):
        X[i] = 0

ans = 0
for i in range(N):
    if X[A[i]] == 1:
        ans += 1
print(ans)
