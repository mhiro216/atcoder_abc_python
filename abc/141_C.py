import sys
sys.setrecursionlimit(10**6)
n,k,q = map(int, input().split())
readline = sys.stdin.readline
A = [int(input()) for i in range(q)]

score = [k-q for i in range(n)]
for a in A:
    score[a-1] += 1
for s in score:
    if s > 0:
        print('Yes')
    else:
        print('No')