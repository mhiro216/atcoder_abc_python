import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,k = [int(i) for i in readline().split()]

def Base_10_to_k(n, k):
    if int(n/k): return Base_10_to_k(int(n/k), k)+str(n%k)
    return str(n%k)

print(len(Base_10_to_k(n, k)))