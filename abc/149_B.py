a,b,k = list(map(int, input().split()))

if a <= k:
    k -= a
    a = 0
else:
    a -= k
    k = 0

if b <= k:
    b = 0
else:
    b -= k
    
print(a, b)