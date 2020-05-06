n,k = list(map(int, input().split()))

def Base_10_to_k(n, k):
    if int(n/k): return Base_10_to_k(int(n/k), k)+str(n%k)
    return str(n%k)

print(len(Base_10_to_k(n, k)))