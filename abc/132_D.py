"""
組み合わせ, nCrのmod
"""

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

mod = 10**9+7

def choose(n,r):
    p,q = 1,1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p * pow(q,mod-2,mod) % mod # modの世界では逆元はpow(x,mod-2)をかけることと同じ

ans = []
for i in range(1,k+1):
    comb_div = choose(k-1, i-1) # k個の青いボールをiグループに分ける分け方。(1,2)と(2,1)は後で赤いボールに混ぜるときに違う並べ方になるので違うものとみなす
    comb_loc = choose(n-k+1, i) * comb_div % mod # iグループの青いボールを赤いボールに混ぜる混ぜ方。混ぜる場所の組み合わせを求めた上で、グループの分け方の数を乗じる
    ans.append(comb_loc)
    
print(*ans)