n,m = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort(reverse=True)
total = sum(a)
if a[m-1] < total/(4*m):
    print('No')
else:
    print('Yes')