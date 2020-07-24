## 再帰関数　階乗計算

n = 5

def fact(n):
    if n == 0: return 1
    return n * fact(n-1)

print(fact(n))