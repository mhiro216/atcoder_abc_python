n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

import itertools

a = [i+1 for i in range(n)]

C = list(itertools.permutations(a))

idxs = []

for i, c in enumerate(C):
    l = list(c)
    if l == p:
        idxs.append(i)
    if l == q:
        idxs.append(i)

ans = idxs[1]-idxs[0]

print(ans)