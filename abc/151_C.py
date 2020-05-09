import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,m = [int(i) for i in readline().split()]
ps = []
for _ in range(m):
    p,s = [i for i in readline().split()]
    ps.append([int(p),s])

acs = 0
was = 0
solved = {}
fail_cnt = {}
for p,s in ps:
    if p in solved and solved[p] == 1:
        pass
    elif p in solved and solved[p] == 0 and s == 'AC':
        acs += 1
        solved[p] = 1
        was += fail_cnt[p]
    elif p in solved and solved[p] == 0 and s == 'WA':
        fail_cnt[p] += 1
    elif s == 'AC':
        acs += 1
        solved[p] = 1
    else:
        solved[p] = 0
        fail_cnt[p] = 1
print(acs, was)