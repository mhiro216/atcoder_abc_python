## saruman's army

N = 6
R = 10
X = [1,7,15,20,30,50]

def sarumans_army():
    X.sort()
    
    i = 0; ans = 0
    while i < N:
        # sはカバーされていない一番左の点の位置
        s = X[i]
        i += 1
        # sから距離Rを超える点まで進む
        while i < N and X[i] <= s + R:
            i += 1
        
        # pは新しく印を付ける点の位置
        p = X[i-1]
        # pから距離Rを超える点まで進む
        while i < N and X[i] <= p + R:
            i += 1
            
        ans += 1
        
    return ans

print(sarumans_army())