"""
deque
"""
n,k = list(map(int, input().split()))
p = list(map(int, input().split()))

from collections import deque

p = [(i+1)/2 for i in p]

d_front = deque(p[:k])
d_back = deque(p[k:])

sum_prev = sum(d_front)
ans = sum_prev

while d_back:
    ff = d_front.popleft()
    bf = d_back.popleft()
    sum_curr = sum_prev - ff + bf
    ans = max(ans, sum_curr)
    d_front.append(bf)
    sum_prev = sum_curr
    
print('{:.10f}'.format(ans))