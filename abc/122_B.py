import sys
sys.setrecursionlimit(10**6)

s = input()

l = ['A','C','G','T'] 

ans = 0
tmp = 0

for ch in s:
    if ch in l:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans, tmp)
        
print(ans)