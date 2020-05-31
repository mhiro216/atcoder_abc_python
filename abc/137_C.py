import sys
sys.setrecursionlimit(10**6)

n = int(input())

d = {}

for i in range(n):
    t = input()
    t = ''.join(sorted(t))
    d[t] = d.get(t,0) + 1
        
ans = 0

for v in d.values():
    ans += v*(v-1)//2
    
print(ans)