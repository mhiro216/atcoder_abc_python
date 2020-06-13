import sys
sys.setrecursionlimit(10**6)

n = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p)
swap_pre = []

for i,j in zip(p, p_sorted):
    if i != j and not swap_pre:
        swap_pre += [i,j]
    elif i != j and swap_pre == [j, i]:
        pass
    elif i != j:
        print('NO')
        break
else:
    print('YES')