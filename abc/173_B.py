import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = [input() for _ in range(n)]

d = {'AC':0,'WA':0,'TLE':0,'RE':0}

for i in s:
    d[i] = d.get(i,0) + 1

for k,v in d.items():
    print(k+' x '+str(v))