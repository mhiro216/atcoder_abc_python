import sys
sys.setrecursionlimit(10**6)

k, x = map(int, input().split())

start = x+1-k
end = x+k

ans = [i for i in range(start, end)]

print(*ans)