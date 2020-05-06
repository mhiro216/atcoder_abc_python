a,b = list(map(int, input().split()))

for i in range(10000):
    if i * 8 // 100 == a and i * 10 // 100 == b:
        print(i)
        break
else:
    print(-1)
