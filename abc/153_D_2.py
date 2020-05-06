h = int(input())

def func(x):
    if x == 1:
        return 1
    else:
        a = func(x//2)
        return a*2+1

print(func(h))