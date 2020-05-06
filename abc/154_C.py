n = int(input())
a = list(map(int, input().split()))

sa = set(a)
if len(sa) == n:
    print('YES')
else:
    print('NO')