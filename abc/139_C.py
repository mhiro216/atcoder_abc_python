import sys
sys.setrecursionlimit(10**6)

n = int(input())
h = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0
print(ans)