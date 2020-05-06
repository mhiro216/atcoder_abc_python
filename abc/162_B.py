import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
N = int(readline())

def sum(l, r, d):
    return (l+r)*((r-l)//d+1)//2

print(sum(1,N,1) - sum(3,N-N%3,3) - sum(5,N-N%5,5) + sum(15,N-N%15,15))