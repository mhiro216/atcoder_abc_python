import sys
sys.setrecursionlimit(10**6)

n = int(input())
d = list(map(int, input().split()))

s = sum(d)
ans = 0

for i in d:
    ans += i*(s-i)
ans //= 2

print(ans)