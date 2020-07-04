import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
#n, m = map(int, input().split())
s = input()
t = input()
#s,t = input().split()
#a = [int(input()) for _ in range(n)]
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]

ans = 0

for ch1,ch2 in zip(s,t):
    if ch1 != ch2:
        ans += 1
        
print(ans)