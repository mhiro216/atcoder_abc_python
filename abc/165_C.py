"""
dfs
"""
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,m,q = [int(i) for i in readline().split()]
abcd = [[int(i) for i in readline().split()] for _ in range(q)]

ans = 0

def dfs(A):
    if len(A) == n:
        now = 0
        for a, b, c, d in abcd:
            if A[b-1] - A[a-1] == c: # a,bは1始まりの値になっているので、indexとして使う時は-1する
                now += d
        global ans
        ans = max(ans, now)
    else:
        for i in range(A[-1], m+1):
            dfs(A+[i])

for i in range(1, m+1):
    dfs([i])

print(ans)

#for i in range(1,m+1)のi=1のループ
#A = [1]
#
#A=[1]に対して、for i in range(A[-1], m+1)のi=1のループ
#A = [1, 1]
#
#A=[1, 1]に対して、for i in range(A[-1], m+1)のi=1のループ
#A = [1, 1, 1]
#
#A=[1, 1, 1]に対して、for i in range(A[-1], m+1)のi=1のループ
#A = [1, 1, 1, 1]
#
#A=[1, 1, 1]に対して、for i in range(A[-1], m+1)のi=2のループ
#A = [1, 1, 1, 2]
#
#A=[1, 1, 1]に対して、for i in range(A[-1], m+1)のi=3のループ
#A = [1, 1, 1, 3]
#
#A=[1, 1, 1]に対して、for i in range(A[-1], m+1)のi=4のループ
#A = [1, 1, 1, 4]
#
#A=[1, 1, 1]に対して、for i in range(A[-1], m+1)のi=5のループ
#A = [1, 1, 1, 5]
#
#A=[1, 1, 1]に対して、for i in range(A[-1], m+1)のi=6のループ
#A = [1, 1, 1, 6]
#
#A=[1, 1]に対して、for i in range(A[-1], m+1)のi=2のループ
#A = [1, 1, 2]
#
#以降、Aは以下の順に全探索される
#A = [1, 1, 2, 2]
#A = [1, 1, 2, 3]
#A = [1, 1, 2, 4]
#A = [1, 1, 2, 5]
#A = [1, 1, 2, 6]
#A = [1, 1, 3]
#A = [1, 1, 3, 3]
#A = [1, 1, 3, 4]
#A = [1, 1, 3, 5]
#A = [1, 1, 3, 6]
#A = [1, 1, 4]
#A = [1, 1, 4, 4]
#A = [1, 1, 4, 5]
#A = [1, 1, 4, 6]
#A = [1, 1, 5]
#A = [1, 1, 5, 5]
#A = [1, 1, 5, 6]
#A = [1, 1, 6]
#A = [1, 1, 6, 6]
#A = [1, 2]
#A = [1, 2, 2]
#A = [1, 2, 2, 2]
#A = [1, 2, 2, 3]
#A = [1, 2, 2, 4]
#A = [1, 2, 2, 5]
#A = [1, 2, 2, 6]
#A = [1, 2, 3]
#A = [1, 2, 3, 3]
#A = [1, 2, 3, 4]
#A = [1, 2, 3, 5]
#A = [1, 2, 3, 6]
#A = [1, 2, 4]
#A = [1, 2, 4, 4]
#A = [1, 2, 4, 5]
#A = [1, 2, 4, 6]
#A = [1, 2, 5]
#A = [1, 2, 5, 5]
#A = [1, 2, 5, 6]
#A = [1, 2, 6]
#A = [1, 2, 6, 6]
#A = [1, 3]
#A = [1, 3, 3]
#A = [1, 3, 3, 3]
#A = [1, 3, 3, 4]
#A = [1, 3, 3, 5]
#A = [1, 3, 3, 6]
#A = [1, 3, 4]
#A = [1, 3, 4, 4]
#A = [1, 3, 4, 5]
#A = [1, 3, 4, 6]
#A = [1, 3, 5]
#A = [1, 3, 5, 5]
#A = [1, 3, 5, 6]
#A = [1, 3, 6]
#A = [1, 3, 6, 6]
#A = [1, 4]
#A = [1, 4, 4]
#A = [1, 4, 4, 4]
#A = [1, 4, 4, 5]
#A = [1, 4, 4, 6]
#A = [1, 4, 5]
#A = [1, 4, 5, 5]
#A = [1, 4, 5, 6]
#A = [1, 4, 6]
#A = [1, 4, 6, 6]
#A = [1, 5]
#A = [1, 5, 5]
#A = [1, 5, 5, 5]
#A = [1, 5, 5, 6]
#A = [1, 5, 6]
#A = [1, 5, 6, 6]
#A = [1, 6]
#A = [1, 6, 6]
#A = [1, 6, 6, 6]
#A = [2]
#A = [2, 2]
#A = [2, 2, 2]
#A = [2, 2, 2, 2]
#A = [2, 2, 2, 3]
#A = [2, 2, 2, 4]
#A = [2, 2, 2, 5]
#A = [2, 2, 2, 6]
#A = [2, 2, 3]...