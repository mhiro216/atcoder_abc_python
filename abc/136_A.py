import sys
sys.setrecursionlimit(10**6)

sa, b, c = map(int, input().split())

if b+c > a:
    print(b+c-a)
else:
    print(0)