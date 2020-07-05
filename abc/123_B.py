import sys
sys.setrecursionlimit(10**6)

import math

a2e = [int(input()) for _ in range(5)]

def get_ceiled_num(num):
    ret = math.ceil(num/10)*10
    return ret

ceiled_a2e = [get_ceiled_num(i) for i in a2e]
tot = sum(ceiled_a2e)

ans = tot

for i,j in zip(a2e, ceiled_a2e):
    tmp = tot-(j-i)
    ans = min(ans, tmp)
    
print(ans)