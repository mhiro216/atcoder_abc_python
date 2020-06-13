import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

if (a-b)%2 == 0:
    print((a+b)//2)
else:
    print('IMPOSSIBLE')