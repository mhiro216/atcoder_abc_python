## 二分探索 くじびき

n = 3
m = 10
k = [1,3,5]

def binary_search(k, x):
    l = 0; r = n
    
    # 探索範囲に何も含まれなくなるまで繰り返す
    while r-l >= 1:
        i = int((l+r)/2)
        if k[i] == x:
            return True # 探索対象発見
        elif k[i] < x:
            l = i + 1
        else:
            r = i
    
    return False # 探索対象発見できず

def kujibiki():
    # 二分探索を行うためにソート
    k.sort()
    
    f = False
    
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if binary_search(k, m-k[a]-k[b]-k[c]):
                    f = True
                    
    return f

print(kujibiki())

## 二分探索 くじびき 高速化

n = 3
m = 10
k = [1,3,5]
kk = [0]*(len(k)*len(k))

def fast_binary_search(x):
    l = 0; r = n*n
    
    # 探索範囲に何も含まれなくなるまで繰り返す
    while r-l >= 1:
        i = int((l+r)/2)
        if kk[i] == x:
            return True # 探索対象発見
        elif kk[i] < x:
            l = i+1
        else:
            r = i
            
    return False # 探索対象発見できず

def fast_kujibiki():
    # k[c]+k[d]の取り得る数を列挙
    for c in range(n):
        for d in range(n):
            kk[c*n+d] = k[c] + k[d]
    
    # 二分探索を行うためにソート
    kk.sort()
    
    f = False
    
    for a in range(n):
        for b in range(n):
            if fast_binary_search(m-k[a]-k[b]):
                f = True
            
    return f

print(fast_kujibiki())