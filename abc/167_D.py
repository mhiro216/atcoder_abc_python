n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

init = [1]
len_loop = -1
i = 0

while len(init) <= k:
    nxt = a[init[-1]-1]
    if nxt in init:
#        idx_nxt = init.index(nxt, init[i], init[-1])
        idx_nxt = init.index(nxt)
        len_init = idx_nxt
        len_loop = len(init) - idx_nxt
        break
    else:
        init.append(nxt)
    i += 1

if len_loop == -1:
    print(init[k])
else:
    idx = (k-len_init)%len_loop
    print(init[len_init+idx])