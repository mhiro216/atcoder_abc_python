import sys
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))

CurrentMoney = 1000

for i in range(0, n-1):
    Stocks = 0
    if A[i] < A[i+1]: Stocks = CurrentMoney // A[i]
    CurrentMoney += (A[i+1] - A[i]) * Stocks

print(CurrentMoney)