import sys
sys.setrecursionlimit(10**6)

n = int(input())
d = list(map(int, input().split()))

if n%2 == 0:
    d.sort()
    d_pre = d[n//2-1]
    d_nex = d[n//2]
    print(d_nex - d_pre)
else:
    print(0)