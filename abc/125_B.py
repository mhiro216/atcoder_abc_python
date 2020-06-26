import sys
sys.setrecursionlimit(10**6)

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0

for i,j in zip(v,c):
    if i > j:
        ans += i-j
        
print(ans)