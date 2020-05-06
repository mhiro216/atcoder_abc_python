"""
 floor(a/b) 
=(a-a%b)/b
上を利用して与えられた式を変形すると
max (a(x%b)-(ax%b)) / b
ここで
ax%b = a(x%b)%b
つまり、axをbで割った余りは、xをbで割った余りにaをかけたものを、bで割った余り
を利用すると
max (a(x%b)-a(x%b)%b) / b
つまりa(x%b)、さらに言えばx%bを最大化すれば良い

x%bを最大化するには
n>=b-1 のときは　x=b-1
n<b-1　のときは x=n
"""
a,b,n = list(map(int, input().split()))

if n >= b-1:
    x = b-1
else:
    x = n

ans = a*x//b - a*(x//b)

print(ans)