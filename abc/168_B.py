import sys
sys.setrecursionlimit(10**6)
k = int(input())
s = input()

if len(s) <= k:
    pass
else:
    s = s[:k]+'...'
print(s)