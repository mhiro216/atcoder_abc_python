import sys
sys.setrecursionlimit(10**6)

#a = int(input())
#b = list(map(int, input().split()))
#n, m = map(int, input().split())
#s = input()
#s,t = input().split()
#
#readline = sys.stdin.readline
#n,m = [int(i) for i in readline().split()]
#ab = [[int(i) for i in readline().split()] for _ in range(n)]



"""素因数分解"""
pf = {}

for i in range(2,int(n**0.5)+1):
    while n % i == 0:
        pf[i] = pf.get(i,0) + 1
        n //= i
if n > 1: pf[n] = 1