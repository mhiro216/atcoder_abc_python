"""
素数判定

エラトステネスの篩：
x^(1/2)以下の素数が既知のとき、x^(1/2)以上x以下の素数を決定するには、x以下の整数でx^(1/2)以下の素数の倍数を全て取り除けば（=篩えば）よい
"""
x = int(input())

while True:
    prime_flag = True
    for i in range(2, int(x**0.5+1)):
        if x%i == 0:
            prime_flag = False
            break
    if prime_flag:
        break
    else:
        x += 1
        
print(x)