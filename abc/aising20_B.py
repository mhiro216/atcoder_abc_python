import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

ID = [i for i in range(1,n+1)]

ans = 0

for i,a in zip(ID, A):
    if i%2 == 1 and a%2 == 1:
        ans += 1
        
print(ans)