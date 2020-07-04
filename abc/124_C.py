import sys
sys.setrecursionlimit(10**6)

s = [int(ch) for ch in input()]

ans = [0]*2

for t in range(2):
    tmp = s[:]
    if t == 0:
        for i in range(len(s)-1):
            if i == 0 and tmp[i] == tmp[i+1]:
                tmp[i+1] ^= 1
                ans[t] += 1
            elif i == 0 and tmp[i] != tmp[i+1]:
                pass
            elif tmp[i] == tmp[i+1]:
                tmp[i+1] ^= 1
                ans[t] += 1
    if t == 1:
        for i in range(len(s)-1):
            if i == 0 and tmp[i] == tmp[i+1]:
                tmp[i] ^= 1
                ans[t] += 1
            elif i == 0 and tmp[i] != tmp[i+1]:
                tmp[i] ^= 1
                tmp[i+1] ^= 1
                ans[t] += 2
            elif tmp[i] == tmp[i+1]:
                tmp[i+1] ^= 1
                ans[t] += 1

print(min(ans))