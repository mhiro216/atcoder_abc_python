"""
ビット演算, XOR

XORは桁ごとに独立して計算できるので、桁ごとに計算する
XORが1になるのは0と1を足した時。2つの数を足す時、一方の数のi桁目が1でもう一方の数のi桁目が0であれば、2つの数を足した時のi桁目が1になる
全部で数がn個あるとき、i桁目が1の数がx個ある場合は、i桁目が0の数がn-x個あることになるので、x*(n-x)個の組み合わせでi桁目のXORが1になる

注：以下はPythonではTLEでしたがPyPyでACでした
"""

n = int(input())
a = list(map(int, input().split()))

MOD = 10**9+7
ans = 0

for i in range(60):
    x = 0 # i桁目が1である数の個数
    for j in range(n):
        if a[j]>>i&1: # "a[j]のi桁目が1である"という意味
            x += 1
    now = x*(n-x)%MOD
    for j in range(i):
        now = now*2%MOD # 2**60をかけると容易にオーバーフローするので、安全に2をかけるごとにMODをとっている
    ans += now
    ans %= MOD
    
print(ans)