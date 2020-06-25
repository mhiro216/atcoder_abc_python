import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = input()

s = [ch for ch in s]
s[k-1] = s[k-1].lower()
s = ''.join(s)

print(s)