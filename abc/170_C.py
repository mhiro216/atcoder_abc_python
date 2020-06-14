import sys
sys.setrecursionlimit(10**6)

x, n = map(int, input().split())

if n != 0:
    p = list(map(int, input().split()))

    ll = [x]
    lu = [x]
    i = 1
    
    for _ in range(2*n):
        if ll[-1] not in p:
            print(ll[-1])
            break
        elif lu[-1] not in p:
            print(lu[-1])
            break
        ll.append(ll[-1]-i)
        lu.append(lu[-1]+i)
else:
    print(x)