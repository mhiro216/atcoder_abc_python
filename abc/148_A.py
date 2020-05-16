a = int(input())
b = int(input())

ans = 0

for i in [1,2,3]:
    if i not in [a,b]:
        ans = i

print(ans)