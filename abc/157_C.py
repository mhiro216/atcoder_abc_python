import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,m = [int(i) for i in readline().split()]
sc = [[int(i) for i in readline().split()] for _ in range(m)]

ans = [0]*n

for s,c in sc:
    if n >= 2 and s-1 == 0 and c == 0: # 2桁以上の数で、左から1桁目が0を指定された場合は-1
        print(-1)
        break
    elif ans[s-1] == 0:
        ans[s-1] = c
    elif ans[s-1] != c: # 左からs桁目が異なる値を指定された場合は-1
        print(-1)
        break
else:
    if n >= 2 and ans[0] == 0:
        ans[0] = 1
    ans = sum([10**(n-i-1)*d for i,d in enumerate(ans)])
    print(ans)