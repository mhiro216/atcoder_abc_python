import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

tmp = sum([1/a for a in A])
print(1/tmp)