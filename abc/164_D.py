s = input()[::-1] # 右からn桁の数についてループを回していきたいので、文字列を反転させる

sum_of_digits = 0 # 余りの値
cnts = [0] * 2019 # 余りの値ごとに余りが同じ値の数を格納する変数。2019で割る場合、余りは0~2018までの2019通りあるので、リストの長さは2019
cnts[0] = 1 # ※1
d = 1 # sum_of_digitsの計算に使う10の累乗値

# まず余りの値ごとに余りが同じ値の数を数える
for c in s:
    sum_of_digits += int(c) * d
    sum_of_digits %= 2019
    d *= 10
    d %= 2019 # ※2
    cnts[sum_of_digits] += 1

# 次に余りの値ごとにその組み合わせを計算し、足し合わせる
ans = 0
for cnt in cnts:
    ans += cnt * (cnt - 1) // 2

print(ans)