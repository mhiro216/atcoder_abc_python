"""
x = ai(p+0.5)
0.5が入っていると整数として扱いづらいので、aiが偶数であることを利用して以下のように変形
x = ai'(2p+1)
ai' = 2ai
ここで2p+1が奇数であることから、xおよびai'が2で割れる回数は同じでなければならない。
2で割れる回数をtとすると、
x' = ai''(2p+1)
x' = x/(2^t)
ai'' = ai'/(2^t)
Mも2^tで割っておく。
M' = M/(2^t)
Xとして何が考えられるかは、まずai''の最小公倍数Lが考えられる
lcm(ai'') = L
さらに、Lの奇数倍も考えられる
したがって答えは、M'/2Lの小数点以下切り上げたもの

（以下サンプルによる実験）
M = 100, a = [12, 20] で考えてみる

X = 12*(p+0.5)
X = 20*(p+0.5)

X = 12*(2p+1)
X = 20*(2p+1)

X = (2^1*3)*(2p+1)
X = (2^1*5)*(2p+1)

両辺を2^1で割る
X' = X/(2^1)
とすると
X' = 3*奇数
X' = 5*奇数

X'がとり得る値は、まず3と5の最小公倍数である15。その奇数倍(15,45,75...)も満たす
ただしXはM以下である必要があるので、X'はM'=M/(2^1)以下、つまり50以下である必要がある
よってX'がとり得る値は、15,45の2つ

Xがとり得る値は、30,90の2つ
検算すると
30 = 12*(2+0.5)
30 = 20*(1+0.5)
90 = 12*(7+0.5)
90 = 20*(4+0.5)
"""

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

def func(x):
    """2で割れる回数を求める"""
    res = 0
    while x%2 == 0:
        x //= 2
        res += 1
    return res

#from math import gcd # v3.5以降
from fractions import gcd # v3.4以前
from functools import reduce

def lcm_base(x, y):
    """2つの値の最小公倍数"""
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    """3つ以上の値の最小公倍数"""
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    """3つ以上の値の最小公倍数"""
    return reduce(lcm_base, numbers, 1)

def main(n,m,a):
    ans = 0
    # a -> a'
    for i in range(n):
        if a[i]%2 == 1:
            print(0)
            return
        a[i] //= 2

    # a' -> a''
    t = func(a[0])
    for i in range(n):
        if func(a[i]) != t:
            print(0)
            return
        a[i] >>= t # シフト演算 a[i] //= 2^t
    m >>= t

    l = 1
    for i in range(n):
        l = lcm(l, a[i])
        if l > m:
            print(0)
            return

    m //= l
    ans += (m+1)//2
    print(ans)
    
main(n,m,a)