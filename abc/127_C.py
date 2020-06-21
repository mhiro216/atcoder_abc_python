import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

L = []; R = []
for _ in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

maxL = max(L)
minR = min(R)

ans = max(0, minR-maxL+1)
print(ans)