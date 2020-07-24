## 区間スケジューリング

N = 5
S = [1,2,4,6,8]
T = [3,5,7,9,10]
itv = [[0]*2 for i in range(N)] # [[0,0]*N]はダメ https://note.nkmk.me/python-list-initialize/

def scheduling():
    # 終了時間の早い順にしたいため、Tを各配列の1番目に、Sを2番目に入れる
    for i in range(N):
        itv[i][0] = T[i]
        itv[i][1] = S[i]
    itv.sort() # 終了時間の早い順にソートする（.sort()は要素の1番目でソートする）
    
    # tは最後に選んだ仕事の終了時間
    ans = 0; t = 0
    for i in range(N):
        if t < itv[i][1]:
            ans += 1
            t = itv[i][0]
            
    return ans

print(scheduling())