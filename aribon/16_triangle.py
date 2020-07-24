## 3つの棒で三角形を作る

n, a = 5, [2,3,4,5,10]
n, a = 4, [4,5,10,20]

def triangle():
    ans = 0
    
    for i in range(0,n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                le = a[i] + a[j] + a[k] # 周長
                ma = max(a[i], a[j], a[k]) # 最も長い棒の長さ
                rest = le - ma # 他の2本の棒の長さの和
                
                if ma < rest:
                    # 三角形が作れる関係にあるので、答えを更新できれば更新
                    ans = max(ans, le)
                    
    return ans

print(triangle())