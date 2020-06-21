import sys
sys.setrecursionlimit(10**6)

w, h, x, y = map(int, input().split())

ans1 = w*h/2
ans2 = 0

if x == w/2 and y == h/2:
    ans2 = 1

print(ans1, ans2)
