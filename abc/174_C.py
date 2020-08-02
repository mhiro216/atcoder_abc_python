import sys
sys.setrecursionlimit(10**6)

k = int(input())

mod = 7 % k
for i in range(1, k*2):
    if mod == 0:
        print(i)
        break
    mod = (mod * 10 + 7) % k
else:
    print(-1)