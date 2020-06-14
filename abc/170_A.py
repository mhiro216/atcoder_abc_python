import sys
sys.setrecursionlimit(10**6)

x = list(map(int, input().split()))

print(x.index(0)+1)