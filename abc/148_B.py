n = int(input())
s, t = input().split()

ans = ''

for i,j in zip(s,t):
    ans += i+j
    
print(ans)