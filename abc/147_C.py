import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n = int(input())
a = []
xy = []
for _ in range(n):
    tmp_a = int(input())
    tmp_xy = [[int(i) for i in readline().split()] for _ in range(tmp_a)]
    a.append(tmp_a)
    xy.append(tmp_xy)
    
from itertools import product

ans_list = []

for comb in product([1,0], repeat=n):
    lie_list = [-1]*n
    flag = True
    for i in range(n):
        if comb[i] == 1:
            if lie_list[i] == -1:
                lie_list[i] = 1
            elif lie_list[i] == 1:
                pass
            elif lie_list[i] != 1:
                flag = False
                break
            for x,y in xy[i]:
                if lie_list[x-1] == -1:
                    lie_list[x-1] = y
                elif lie_list[x-1] == y:
                    pass
                elif lie_list[x-1] != y:
                    flag = False
                    break
        else:
            if lie_list[i] == -1:
                lie_list[i] = 0
            elif lie_list[i] == 0:
                pass
            elif lie_list[i] != 0:
                flag = False
                break
    if flag:
        ans_list.append(sum(comb))

if ans_list:
    print(max(ans_list))
else:
    print(0)