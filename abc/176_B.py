import sys
sys.setrecursionlimit(10**6)

n = int(input())

str_n = str(n)

tot = 0

for ch in str_n:
    tot += int(ch)

if tot % 9 == 0:
    print('Yes')
else:
    print('No')
