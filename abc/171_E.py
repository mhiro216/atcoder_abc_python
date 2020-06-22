"""
keyword: XOR

求める各整数をniとする

niを求めるには、i!=jのすべてのajのXORをとれば良い
なぜなら、i!=jのすべてのajのXORをとると、自分以外のnjは全て偶数回XORがとられて0に消し込まれる一方、niだけは奇数回XORがとられるので残る

つまり、i=1の整数n1は、
n1 = a2 ^ a3 ^ ... ^ an
と求められる

残りのniを求めるにあたっては、i=2を例にとれば、
n2 = a1 ^ a3 ^ ... ^ an
となることから、
n2 = n1 ^ a1 ^ a2
とすれば求まることに注意
"""

import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

su = 0

for i in range(1, n):
    su ^= a[i]
    
ans = [su]

for i in range(n-1):
    su ^= a[i] ^ a[i+1]
    ans.append(su)
    
print(*ans)