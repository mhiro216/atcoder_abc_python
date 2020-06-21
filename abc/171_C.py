import sys
sys.setrecursionlimit(10**6)

n = int(input())

d = {(i-97+1)%26:chr(i) for i in range(97,97+26)}

l = []

while n > 0:
    tmp = n%26
    l.append(tmp)
    if tmp == 0:
        n = n//26-1
    else:
        n //= 26

ans = ''

for i in l[::-1]:
    ans += d[i]
    
print(ans)