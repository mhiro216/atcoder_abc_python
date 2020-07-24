## Ants

L = 10
n = 3
x = [2,6,7]

def ants():
    minT = 0
    for i in range(n):
        minT = max(minT, min(x[i], L-x[i]))
        
    maxT = 0
    for i in range(n):
        maxT = max(maxT, max(x[i], L-x[i]))
        
    return minT, maxT

print(ants())