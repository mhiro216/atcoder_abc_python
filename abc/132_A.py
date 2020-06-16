import sys
sys.setrecursionlimit(10**6)

s = input()

d = {}

for ch in s:
    d[ch] = d.get(ch, 0) + 1
    
if len(d) == 2:
    for k in d:
        if d[k] == 2:
            pass
        else:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')