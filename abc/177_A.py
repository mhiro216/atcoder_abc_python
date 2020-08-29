import sys
sys.setrecursionlimit(10**6)

d, t, s = map(int, input().split())

if d/s <= t:
    print('Yes')
else:
    print('No')
