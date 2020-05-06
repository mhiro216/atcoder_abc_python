n = int(input())

def func(x):
    a = x%10
    b = 0
    while x:
        b = x
        x //= 10
    return (a,b)

freq = {}

for i in range(1, n+1):
    p = func(i)
    freq[p] = freq.get(p, 0) + 1

ans = 0

for i in range(1, n+1):
    p = func(i)
    ans += freq.get((p[1],p[0]), 0)
    
print(ans)