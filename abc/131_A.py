import sys
sys.setrecursionlimit(10**6)

s = input()

ch_prev = ''
for ch in s:
    if ch_prev and ch == ch_prev:
        print('Bad')
        break
    else:
        ch_prev = ch
else:
    print('Good')