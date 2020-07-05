"""
二重ループ　正解を見つけたらループを止める
"""

import sys
sys.setrecursionlimit(10**6)

a2e = [int(input()) for _ in range(5)]
k = int(input())

for i in a2e:
    for j in a2e:
        if abs(i-j) > k:
            print(':(')
            break
    else:
        continue
    break
else:
    print('Yay!')