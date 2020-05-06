import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,k = [int(i) for i in readline().split()]

a = n%k
ans = min(a, k-a)

print(ans)