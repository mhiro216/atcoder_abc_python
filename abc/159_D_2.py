n = input()
a = list(map(int, input().split()))

def choose2(n):
    return n*(n-1)//2

a = [i-1 for i in a]
cnt = [0]*n
for i in range(n):
    cnt[a[i]] += 1
tot = 0
for i in range(n):
    tot += choose2(cnt[i])
for i in range(n):
    ans = tot
    ans -= choose2(cnt[a[i]])
    ans += choose2(cnt[a[i]]-1)
    print(ans)