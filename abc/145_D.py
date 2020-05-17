"""
組み合わせ, nCrのmod

(i+1, j+2)で動く回数をm回、(i+2, j+1)で動く回数をn回とすると
m + 2n = x
2m + n = y
の方程式の解として、m,nが0以上の整数で求められる必要がある

m,nが0以上の整数で求められなければそのような行き方はない
求められれば、全部でm+n回の動きの中でどのm回で(i+1, j+2)の動きをするか（ないし、どのn回で(i+2, j+1)の動きをするか）が行き方の数なので、m+nCmを求めれば良い
"""
x,y = map(int, input().split())

mod = 10**9+7

def choose(n,r):
    p,q = 1,1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p * pow(q,mod-2,mod) % mod # modの世界では逆元はpow(x,mod-2)をかけることと同じ

n = (2*x-y)/3
m = (y-n)/2

if n >= 0 and m >= 0 and not n%1 and not m%1:
    ans = choose(int(m+n), int(m))
else:
    ans = 0
print(ans)