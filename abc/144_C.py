import sys
sys.setrecursionlimit(10**6)

n = int(input())

ans = 1+n-2

for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        j = n//i
        ans = min(ans, i+j-2)

print(ans)