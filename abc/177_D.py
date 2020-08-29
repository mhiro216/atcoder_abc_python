import queue
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
readline = sys.stdin.readline

f = [set() for _ in range(n)]
ans = [1]*n
seen = [False]*n

for _ in range(m):
    a, b = [int(i) for i in readline().split()]
    a -= 1
    b -= 1
    f[a].add(b)
    f[b].add(a)

q = queue.Queue()

for i in range(n):
    if not seen[i]:
        q.put(i)
        while not q.empty():
            v = q.get()
            seen[v] = True
            for u in f[v]:
                if seen[u]:
                    continue
                ans[v] += 1
                seen[u] = True
                q.put(u)

# print(f)
# print(*ans)
print(max(ans))
