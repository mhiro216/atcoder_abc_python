## 辞書順最小

N = 6
S = 'ACDBCB'

def best_cow_line():
    ans = ''
    
    a = 0; b = N-1
    
    while a <= b:
        # 文字列を左から見た場合と右から見た場合で辞書順比較
        left = False
        for i in range(b-a+1):
            if S[a+i] < S[b-i]: # 最左の文字の方が小さい場合は最左の文字を追加
                left = True
                break
            elif S[a+i] > S[b-i]: # 最右の文字の方が小さい場合は最右の文字を追加
                left = False
                break
        if left:
            ans += S[a]
            a += 1
        else:
            ans += S[b]
            b -= 1
    
    return ans

print(best_cow_line())