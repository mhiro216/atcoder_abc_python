import sys
sys.setrecursionlimit(10**6)
n = int(input())
B = list(map(int, input().split()))

INF = 1001001001
B = [INF]+B+[INF]

ans = 0
for i in range(n):
    ans += min(B[i],B[i+1])
print(ans)