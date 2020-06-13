import sys
sys.setrecursionlimit(10**6)

s = input()
s = [ch for ch in s]
n = len(s)

ans = [0]*n

for _ in range(2):
    cnt = 0
    for i in range(n):
        if s[i] == 'R': cnt += 1
        else:
            ans[i] += cnt//2
            ans[i-1] += (cnt+1)//2
            cnt = 0
        
    ans.reverse()
    s = s[::-1]
    for i in range(n):
        if s[i] == 'L': s[i] = 'R'
        else: s[i] = 'L'

print(*ans)