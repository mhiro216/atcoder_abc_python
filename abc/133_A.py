import sys
sys.setrecursionlimit(10**6)

n, a, b = map(int, input().split())

ans = min(a*n, b)

print(ans)