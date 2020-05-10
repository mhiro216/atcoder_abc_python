"""
dp
"""

n, k = [int(i) for i in input().split()]
r, s, p = [int(i) for i in input().split()]
t = input()

hand = {'r':p, 's':r, 'p':s}
ans = 0

for i in range(k):
    last = ''
    j = i
    while j < n:
        aite = t[j]
        if aite != last: # 相手の手がk回前と違ったら、勝ちの手を出せる
            ans += hand[aite]
            last = aite
        else: # 相手の手がk回前と同じなら、勝ちの手は出せない（正確には、k回後に勝てるような手を出しておいた方が良い）
            last = '' # k回後に勝てるような手を出す前提で、nullにしておく（k回後に勝つ手によって変わる値）
        j += k

print(ans)