import sys
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())
k = int(input())

trial = 0

while trial <= k:
    if b > a and c > b:
        print('Yes')
        break
    elif b <= a:
        b *= 2
        trial += 1
    elif c <= b:
        c *= 2
        trial += 1
else:
    print('No')