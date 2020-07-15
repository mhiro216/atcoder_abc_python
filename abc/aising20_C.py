import sys
sys.setrecursionlimit(10**6)

n = int(input())

import math

ans = [0]*n
upper = int(math.sqrt(n))+1

for x in range(1,upper+1):
    for y in range(1,upper+1):
        for z in range(1,upper+1):
            tmp = pow((x+y),2)+pow((y+z),2)+pow((x+z),2)
            if tmp%2 == 0:
                ans[tmp//2] += 1
                
print(*ans)