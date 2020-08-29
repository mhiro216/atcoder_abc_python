import sys
sys.setrecursionlimit(10**6)

s = input()
t = input()

s = [ch for ch in s]
t = [ch for ch in t]

ans = len(t)
if len(s) == len(t):
    tmp = 0
    for i in range(len(t)):
        if s[i] != t[i]:
            tmp += 1
    ans = min(ans, tmp)
else:
    for j in range(len(s)-len(t)):
        tmp = 0
        for i in range(len(t)):
            if s[i+j] != t[i]:
                tmp += 1
        ans = min(ans, tmp)
print(ans)
