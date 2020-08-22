# fence repair

import heapq

N = 3
L = [8, 5, 8]

ans = 0

# 順位キューを用意（小さい数から出てくるように）
que = []
heapq.heapify(que)

for i in range(N):
    heapq.heappush(que, L[i])

# 板が1本になるまで適用
while len(que) > 1:
    # 一番短い板、次に短い板を取り出す
    l1 = heapq.heappop(que)
    l2 = heapq.heappop(que)

    # 併合
    ans += l1 + l2
    heapq.heappush(que, l1+l2)

print(ans)
