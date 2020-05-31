"""
隣り合う2要素を掛けていく

ref. https://atcoder.jp/contests/abc169/submissions/13893064
"""
n = int(input())
A = list(map(int,input().split()))

MX = 1e18

while len(A)>1:
    if len(A)%2 == 1: # 要素数が奇数のときは[1]を加えて偶数にしておく
        A += [1]
    A = [A[2*i]*A[2*i+1] for i in range(len(A)//2)]

if A[0] > MX:
    print(-1)
else:
    print(A[0])
