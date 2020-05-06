import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
a,b = [int(i) for i in readline().split()]

for i in range(10000):
    if i * 8 // 100 == a and i * 10 // 100 == b:
        print(i)
        break
else:
    print(-1)
