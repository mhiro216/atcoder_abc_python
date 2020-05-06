import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = readline()
A = [int(i) for i in readline().split()]

d = {}
for a in A:
    d[a] = d.get(a, 0) + 1
total = sum([v*(v-1)/2 for v in d.values()]) 

for i in range(n):
    print(int(total - d[A[i]] + 1))
