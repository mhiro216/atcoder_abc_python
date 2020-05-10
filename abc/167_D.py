"""
dp
"""

n, k = map(int, input().split())
a = tuple(map(lambda n: int(n) - 1, input().split()))

visited = [0] * n
next_town = 0
order = []

while True:
    if visited[next_town]:
        break
    order.append(next_town)
    visited[next_town] = 1
    next_town = a[next_town]

first_loop = len(order)
offset = order.index(next_town)
second_loop = first_loop - offset

if k < first_loop:
    print(order[k] + 1)
else:
    print(order[offset + (k - first_loop) % second_loop] + 1)
