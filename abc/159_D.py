n = input()
A = list(map(int, input().split()))

d = {}
for a in A:
    d[a] = d.get(a, 0) + 1
total = sum([v*(v-1)/2 for v in d.values()]) 

for i in range(n):
    print(int(total - d[A[i]] + 1))
