"""二分探索"""

a,b,x = map(int, input().split())

def func(x):
    """桁数を返す"""
    if x == 0: return 1
    ret = 0
    while x:
        x //= 10
        ret += 1
    return ret

l = 0; r = 10**9+1 # 二分探索時は探索範囲は取り得る値+-1しておく

while l+1 < r:
    c = (l+r)//2
    if a*c+b*func(c) <= x:
        l = c
    else:
        r = c

print(l)