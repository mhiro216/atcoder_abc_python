"""
keyword: 二項係数, 冪乗のmod

与えられた文字列sの最後の文字以降は何を置いても(26通り)良い一方で、最後の文字より前は同じ文字は置けない(25通り)
そこで最後の文字より後と前で分けて場合の数を考える

pow(x, y, z) は pow(x, y) % z よりも高速で処理されるので、こちらを使う

pythonでTLE, pypyでAC
"""

import sys
sys.setrecursionlimit(10**6)

k = int(input())
s = input()

mod = 10**9+7

n = len(s)
fact = [1, 1] # あとでnの階乗を求める初期値　[0!, 1!]

# n!を求める
for i in range(2, 2*(10**6)+1):
    fact.append(fact[-1]*i % mod)

# 二項係数nCrを求める nCr = n!/r!(n-r)!
def nCr(n, r, mod=10**9+7):
    return pow(fact[n-r]*fact[r] % mod, mod-2, mod)*fact[n] % mod # modの世界では逆元はpow(x,mod-2)をかけることと同じ

ans = 0

for i in range(k+1):
    now = pow(26, k-i, mod) * pow(25, i, mod) * nCr(i+n-1, n-1)
    ans = (ans+now) % mod
print(ans)

# 以下でもOK。なぜ？
# for i in range(k+1):
#     ans = (ans+nCr(n+k, i)*pow(25, i, mod)) % mod
# print(ans)