# プライオリティキュー

import heapq

N = 4
L = 25
P = 10
A = [10, 14, 20, 12]
B = [10, 5, 2, 4]

# 簡単のためゴールをガソリンスタンドに追加
A.append(L)
B.append(0)
N += 1

# ガソリンスタンドを管理する順位キュー
que = []
heapq.heapify(que)

# ans:補給回数、pos:今いる場所、tank:タンクのガソリンの量
ans = 0
pos = 0
tank = P

for i in range(N):
    # 次に進む距離
    d = A[i] - pos

    # 次に進むまでにタンクのガソリンがなくなる場合
    while tank-d < 0:
        # プライオリティキューが空だと、移動は達成できないので-1を出力して終了
        if len(que) == 0:
            print(-1)
            exit()
        # プライオリティキューが空でなければ、最も大きい数字を取り出し、そこでガソリンを補給したことにする
        tmp = heapq.heappop(que)
        # tmpは最小値（マイナス）で取れてくるのでマイナスをかけて最大値に戻す
        tank += -tmp
        ans += 1

    # ガソリンスタンドiを通過した際、プライオリティキューに-B[i]を追加（マイナスなのは最大値を最小値として初めに取り出すため）
    tank -= d
    pos = A[i]
    heapq.heappush(que, -B[i])

print(ans)
