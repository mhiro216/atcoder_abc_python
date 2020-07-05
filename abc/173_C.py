import sys
sys.setrecursionlimit(10**6)

import itertools

h, w, k = map(int, input().split())
field = [input() for _ in range(h)]

field = [list(f) for f in field]

black_h = {}
black_w = {}
black_i = {}

tot = 0

for ih in range(h):
    for iw in range(w):
        black_h[ih] = 0
        black_w[iw] = 0
        black_i[(ih,iw)] = 0

for ih in range(h):
    for iw in range(w):
        if field[ih][iw] == '#':
            black_h[ih] += 1
            black_w[iw] += 1
            black_i[(ih,iw)] += 1
            tot += 1
            
#print(black_h)
#print(black_w)
#print(black_i)
#print(tot)

ans = 0

for n_comb_h in range(h+1):
    for v_h in itertools.combinations([i for i in range(h)],n_comb_h):
        for n_comb_w in range(w+1):
            for v_w in itertools.combinations([i for i in range(w)],n_comb_w):
                tmp = 0
                for i_h in v_h:
                    tmp += black_h[i_h]
                for i_w in v_w:
                    tmp += black_w[i_w]
                for i_h in v_h:
                    for i_w in v_w:
                        if black_i[(i_h, i_w)] == 1:
                            tmp -= 1
                if tmp == tot-k:
                    ans += 1
                    
print(ans)