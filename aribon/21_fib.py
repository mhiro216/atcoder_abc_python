## フィボナッチ数列

n = 10

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

print(fib(n))

## フィボナッチ数列　高速化

n = 10
memo = [0]*(n+1)

def fast_fib(n):
    if n <= 1: return n
    if memo[n] != 0: return memo[n]
    memo[n] = fast_fib(n-1) + fast_fib(n-2)
    return memo[n]

print(fast_fib(n))s