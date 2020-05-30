import sys
sys.setrecursionlimit(10**6)

n = int(input())
V = list(map(int, input().split()))

V.sort()
ans = 0

for i,v in enumerate(V):
    if i == 0:
        ans += v/(2**(n-i-1))
    else:
        ans += v/(2**(n-i))

print(ans)