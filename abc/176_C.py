import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

ans = 0
max = 0

for a in A:
    if a >= max:
        max = a
    else:
        ans += max-a

print(ans)
