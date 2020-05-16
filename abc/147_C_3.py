"""再帰"""

N = int(input())
data = []
for _ in range(N):
	A = int(input())
	items = []
	for __ in range(A):
		x, y = map(int, input().split())
		items.append((x - 1, y))
	data.append(items)


best = 0

def check(state):
	for i in range(N):
		if state[i] == 1: # 正直な人の証言にだけ注目すれば良い
			for x, y in data[i]:
				if y != state[x]:
					return False
	return True

def combination(state):
	global best
	if len(state) == N:
		if check(state):
			count = sum(state)
			if count > best:
				best = count
	else:
		combination(state + [0]) # ここでn個の要素が0or1となる2**nパターンを全て列挙している
		combination(state + [1]) # ここでn個の要素が0or1となる2**nパターンを全て列挙している

combination([])

print(best)
