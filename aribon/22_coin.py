## コイン

V = [1, 5, 10, 50, 100, 500]
C = [3, 2, 1, 3, 0, 2]
A = 620

def coin():
    ans = 0
    global A # https://qiita.com/Boccochan/items/16873254cc8a48bd7bb4
    
    for i in range(5, -1, -1):
        t = min(int(A/V[i]), C[i]) # コインiを使う枚数
        A -= t * V[i]
        ans += t
        
    return ans

print(coin())