import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

print(max([a+b, a-b, a*b]))