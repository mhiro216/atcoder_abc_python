import sys
sys.setrecursionlimit(10**6)

n = int(input())
h = list(map(int, input().split()))

ma = 0
ans = 0

for i in range(n):
    if h[i] >= ma:
        ans += 1
    ma = max(ma, h[i])
    
print(ans)