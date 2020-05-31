import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

ans = 1
MX = 1e18

if 0 in A:
    print(0)
else:
    for a in A:
        ans *= a
        if ans > MX:
            print(-1)
            break
    else:
        print(ans)