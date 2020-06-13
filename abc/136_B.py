import sys
sys.setrecursionlimit(10**6)

n = int(input())

l = [i for i in range(1,10)] + [i for i in range(100,1000)] + [i for i in range(10000,100000)] 

n = [i for i in range(1,n+1)]

ans = len(set(l) & set(n))

print(ans)