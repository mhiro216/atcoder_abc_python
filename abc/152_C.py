n = int(input())
p = list(map(int, input().split()))

ans = 1
mini = p[0]

for i in p[1:]:
    mini = min(mini, i)
    if i <= mini:
        ans += 1
        
print(ans)