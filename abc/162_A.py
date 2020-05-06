import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
N = int(readline())

for i in range(3):
    if N % 10 == 7:
        print('Yes')
        break
    else:
        N //= 10
        continue
    break
else:
    print('No')