abc = list(map(int, input().split()))

if len(set(abc)) == 2:
    print('Yes')
else:
    print('No')