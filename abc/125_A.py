import sys
sys.setrecursionlimit(10**6)

a, b, t = map(int, input().split())

ans = 0
A = a

while A <= t+0.5:
    ans += b
    A += a
    
print(ans)