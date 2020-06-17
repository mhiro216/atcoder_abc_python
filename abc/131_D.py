import sys
sys.setrecursionlimit(10**6)

n = int(input())

readline = sys.stdin.readline

d = {} # k:締め切り時間、v:その時までに終わらせるべき仕事量

for _ in range(n):
    a,b = [int(i) for i in readline().split()]
    d[b] = d.get(b, 0) + a

d_sorted = sorted(d.items(), key=lambda x:x[0])

s = 0
for t, w in d_sorted:
    s += w
    if s > t: # 締め切り時間=その時までに終わらせられる最大の仕事量なので、それを仕事量が超えた時点で完了は不可能となる
        print('No')
        break
else:
    print('Yes')