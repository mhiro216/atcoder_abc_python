import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
A = list(map(int, input().split()))
        
for i in range(n-k):
    pos = k+i
    if A[pos] > A[pos-k]:
        print('Yes')
    else:
        print('No')