import sys
sys.setrecursionlimit(10**6)

s = input()

s_low = s.lower()

if s == s_low:
    print('A')
else:
    print('a')