import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,x,y = [int(i) for i in readline().split()]

ans = [0] * n

for a in range(1, n+1):
    for b in range(a+1, n+1):
        d = b - a
        d2 = abs(x-a) + abs(y-b) + 1
        d = d if d < d2 else d2
        ans[d] += 1

for i in range(1, n):
    print(ans[i])