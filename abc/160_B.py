import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
x = int(readline())

ans = 0

ans += x//500*1000
x %= 500

ans += x//5*5

print(ans)