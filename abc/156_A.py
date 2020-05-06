import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,r = [int(i) for i in readline().split()]

if n >= 10:
    print(r)
else:
    print(r+100*(10-n))