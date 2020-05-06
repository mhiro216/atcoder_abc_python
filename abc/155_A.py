import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
abc = [int(i) for i in readline().split()]

if len(set(abc)) == 2:
    print('Yes')
else:
    print('No')