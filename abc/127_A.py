import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

if a <= 5:
    print(0)
elif a >= 13:
    print(b)
else:
    print(b//2)