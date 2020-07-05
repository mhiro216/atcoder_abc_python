import sys
sys.setrecursionlimit(10**6)

n = int(input())
a2e = [int(input()) for _ in range(5)]

ppl = [0]*6
ppl[0] = n

ans = 0

while ppl[-1] != n:
    tmp = ppl[:]
    for i in range(5):
        p = min(ppl[i],a2e[i])
        tmp[i] -= p
        tmp[i+1] += p
    ppl = tmp
    print(ppl)
    ans += 1
    
print(ans)