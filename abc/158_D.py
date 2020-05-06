import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
s = input()
q = int(input())
queries = [[i for i in readline().split()] for _ in range(q)]

from collections import deque

d = deque([i for i in s]) # 要素を前から追加してもO(1)となるようにdeque型に変換
rev = 1 # 今前から読むべきか後ろから読むべきか。逆から読む時は、先頭に文字を追加する操作は末尾からの追加に代わる

for query in queries:
    if query[0] == '1':
        rev *= -1
    else:
        if rev == 1:
            if query[1] == '1':
                d.appendleft(query[2])
            else:
                d.append(query[2])
        else:
            if query[1] == '1':
                d.append(query[2])
            else:
                d.appendleft(query[2])

s = ''.join(d)
if rev == 1:
    print(s)
else:
    print(s[::-1])