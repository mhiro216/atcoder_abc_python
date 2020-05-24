n = int(input())

if n%2 == 0:
    print(0.5)
else:
    n_odd = n//2 + 1
    print(n_odd/n)