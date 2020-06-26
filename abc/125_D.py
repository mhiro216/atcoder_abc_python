"""
符号の反転は2個ずつしかできないので、マイナスの値の個数の偶奇は変わらない。
つまりマイナスの値の個数が偶数であれば必ず0にできるし、奇数であれば必ず1個マイナスの値が残る
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

flip_a = [0]*n
cnt_minus = 0

for i in range(n):
	if a[i] < 0:
		cnt_minus += 1
		flip_a[i] = -a[i]
	else:
		flip_a[i] = a[i]

flip_a.sort()

if cnt_minus%2 == 1:
	flip_a[0] = -flip_a[0]

print(sum(flip_a))