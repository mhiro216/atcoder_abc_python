"""
ルンルン数を列挙すると
1桁：1,2,3,4,5,6,7,8,9
2桁：10,11,12,21,22,23,,,99
となって、一つ下の桁の数に+1or0or-1した値を末尾につけた数を列挙すれば全て列挙できる
例：1 -> 10,11,12
"""
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
k = int(readline())

Xs = [[i for i in range(1, 10)]]
for i in range(9):
    X = []
    for x in Xs[-1]:
        s = x % 10
        if s == 0:
            X.append(x*10+s)
            X.append(x*10+s+1)
        elif s == 9:
            X.append(x*10+s-1)
            X.append(x*10+s)
        else:
            X.append(x*10+s-1)
            X.append(x*10+s)
            X.append(x*10+s+1)
    Xs.append(X)

Xs_concat = []
for x in Xs:
    Xs_concat += x[:]
#Xs_concat.sort() # appendの順番的にsortしなくても既に小さい順に並んでいる

print(Xs_concat[k-1])