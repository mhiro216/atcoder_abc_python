n = int(input())
x = list(map(int, input().split()))

p1 = sum(x)//n
p2 = sum(x)//n+1
ans1 = 0
ans2 = 0
for i in x:
    ans1 += (i-p1)**2
    ans2 += (i-p2)**2
print(min(ans1, ans2))