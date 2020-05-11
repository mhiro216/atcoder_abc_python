n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

from itertools import product
import numpy as np

INF = 1001001001
ans = INF

for i in product(range(2), repeat=n): # product(range(2),n)でn桁のbit全探索が可能
    tmp_price = 0
    tmp_und = np.zeros((m, ))
    for j in range(n):
        if i[j]:
            c, *a = ca[j]
            # Pythonでは、タプルやリストの要素を展開して複数の変数に代入できる。アンパック代入などと呼ばれる
            # 変数の数が要素の数よりも少ない場合、変数名にアスタリスク*をつけると、要素がリストとしてまとめて代入される
            tmp_price += c
            tmp_und += np.array(a, dtype=np.int64)
    tmp_und = tmp_und.tolist() # numpy arrayに対してfor loopをかけるのは遅いのでlistに変換
    if all(tmp_und_ele >= x for tmp_und_ele in tmp_und):
        ans = min(ans, tmp_price)

print(ans if ans != INF else -1)