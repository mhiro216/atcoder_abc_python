import sys
sys.setrecursionlimit(10**6)

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
readline = sys.stdin.readline
A = [[int(i) for i in readline().split()] for _ in range(n)]

ans = 0

for a in A:
    if sum([i*j for i,j in zip(a,b)]) + c > 0:
        ans += 1
        
print(ans)