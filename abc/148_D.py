n = int(input())
a = list(map(int, input().split()))

ans = 0
idx = 1

for i in a:
    if i != idx:
        ans += 1
    else:
        idx += 1

if ans == n:
    print(-1)
else:
    print(ans)