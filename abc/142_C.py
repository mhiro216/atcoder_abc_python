import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

d = {}

for k,v in enumerate(a):
    d[v] = k+1

ans = list(d.values())
    
print(*ans)