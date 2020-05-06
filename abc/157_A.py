import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = int(readline())

print(n//2+n%2)