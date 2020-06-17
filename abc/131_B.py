import sys
sys.setrecursionlimit(10**6)

n, l = map(int, input().split())

li = [i for i in range(l,l+n)]

if 0 in li:
    ans = sum([i for i in range(l,l+n)])
elif li[0] > 0:
    ans = sum([i for i in range(l+1,l+n)])
else:
    ans = sum([i for i in range(l,l+n-1)])
print(ans)