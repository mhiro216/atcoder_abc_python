n = int(input())

def sum(l, r, d):
    return (l+r)*((r-l)//d+1)//2

print(sum(1,n,1) - sum(3,n-n%3,3) - sum(5,n-n%5,5) + sum(15,n-n%15,15))