import sys
sys.setrecursionlimit(10**6)

a,b = map(int, input().split())

if 2*b > a:
    print(0)
else:
    print(a-2*b)