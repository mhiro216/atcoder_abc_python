import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = int(input())
A = [int(i) for i in readline().split()]

for a in A:
    if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
        print('DENIED')
        break
else:
    print('APPROVED')