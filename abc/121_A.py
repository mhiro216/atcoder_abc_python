import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
h, w = map(int, input().split())

ans = H*W - h*W - H*w + h*w
print(ans)