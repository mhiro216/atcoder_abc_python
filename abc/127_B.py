import sys
sys.setrecursionlimit(10**6)

r, d, x = map(int, input().split())

ans = []
for i in range(1,11):
    x = r*x - d
    ans.append(x)
print(*ans)