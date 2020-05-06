import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,a,b = [int(i) for i in readline().split()]

print(n//(a+b)*a + min(n%(a+b),a))