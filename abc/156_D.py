import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,a,b = [int(i) for i in readline().split()]

mod = 10**9+7

def choose(n,r):
    p,q = 1,1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p * pow(q,mod-2,mod) % mod # modの世界では逆元はpow(x,mod-2)をかけることと同じ

ans = (pow(2,n,mod)-1-choose(n,a)-choose(n,b)) % mod

print(ans)