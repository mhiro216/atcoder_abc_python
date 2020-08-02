import sys
sys.setrecursionlimit(10**6)

n = int(input())
C = input()

C = list(C)

d = {0:0}
tot = 0

for i,c in enumerate(C):
    if c == 'R':
        tot += 1
    d[i+1] = tot

ans = tot-d[tot]
print(ans)