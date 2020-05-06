import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,m = [int(i) for i in readline().split()]
a = [int(i) for i in readline().split()]

a.sort(reverse=True)
total = sum(a)
if a[m-1] < total/(4*m):
    print('No')
else:
    print('Yes')