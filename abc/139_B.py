a, b = map(int, input().split())

if b == 1:
    print(0)
else:
    n = 0
    while a + (a-1)*n < b:
        n += 1
    print(n+1)