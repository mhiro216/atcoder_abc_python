import sys
sys.setrecursionlimit(10**6)

n, x = map(int, input().split())
readline = sys.stdin.readline
l = [int(i) for i in readline().split()]

ans = 1
height = 0
for i in range(n):
    height += l[i]
    if height <= x:
        ans += 1
    else:
        break
print(ans)