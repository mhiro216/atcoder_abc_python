n,k,m = list(map(int, input().split()))
a = list(map(int, input().split()))

need = n*m - sum(a)
if need <= 0:
    print(0)
elif need > k:
    print(-1)
else:
    print(need)