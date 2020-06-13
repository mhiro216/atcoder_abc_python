import sys
sys.setrecursionlimit(10**6)

n = int(input())
h = list(map(int, input().split()))

fixed = [False]*n

for i in range(n-1):
    if h[i] < h[i+1]:
        h[i] -= 1
        h[i+1] -= 1
        fixed[i+1] = True
        continue
    elif h[i] == h[i+1]:
        fixed[i+1] = True
        continue
    else:
        print('No')
        break
    break
else:
    print('Yes')