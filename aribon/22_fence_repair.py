# fence repair

N = 3
L = [8, 5, 8]


def fence_repair():
    global N
    ans = 0

    # 板がN本に切断され終わった状態から考えて、板が1本になるまでwhile loopを適用する
    while N > 1:
        # 一番短い板L[mii1], 次に短い板L[mii2]を求める
        mii1 = 0
        mii2 = 1
        if L[mii1] > L[mii2]:
            mii1, mii2 = mii2, mii1

        for i in range(2, N):
            if L[i] < L[mii1]:
                mii2 = mii1
                mii1 = i
            elif L[i] < L[mii2]:
                mii2 = i

        # L[mii1], L[mii2]が求まったので、それらを合計してコストに加算
        t = L[mii1] + L[mii2]
        ans += t

        """
        以降の処理は一見意味が分からないので補足
        
        whileループが進むごとに起こすべき変化（＊）は以下の3つ：
         1. L[mii1]とL[mii2]（一番目と二番目に短い板）を消す
         2. L[mii1]+L[mii2]を加える
         3. Nを1減らす
        例: L=[1,2,3,4]であれば、1,2を消し3を加えて、L=[3,3,4]としたい
         
        ここで、whileループの中でfor i in range(2, N)としているので、L[N-1]はNを1減らした次のループでは参照されることはないことに注目する
        （このように、whileループを進める度に、Lの最後方の値から順に参照されなくなっていく。「なかったことになる」）
        これを利用すると、Lの長さを変えなくとも、＊の変化を起こすことができる
        
        その方法は、L[mii1]をtで置き換え、L[mii2]をL[N-1]で置き換えるというもの
        意図した操作：L=[1,2,3,4] -> L=[3(=1+2),4,3,4]
        L[mii2]をL[N-1]で置き換える操作をしないと、L[N-1]が次のループで参照される対象から外れることに注意する
        意図と異なる操作：L=[1,2,3,4] -> L=[3(=1+2),2,3,4]　次のfor i in range(2, N)のループでは、4が参照されない
        
        また、この方法をとる場合、mii1がN-1の場合は、先にmii1, mii2をswapしておく必要があることに注意する
        
        以上の操作を行うのが以降の処理
        """
        if mii1 == N-1:
            mii1, mii2 = mii2, mii1
        L[mii1] = t
        L[mii2] = L[N-1]
        N -= 1

    return ans


print(fence_repair())
