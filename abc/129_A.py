import sys
sys.setrecursionlimit(10**6)

p, q, r = map(int, input().split())

ans = min([p+q, p+r, q+r])

print(ans)