n = int(input())
s = input()

ans = 0
ch_prev = ''

for ch in s:
    if ch == ch_prev:
        pass
    else:
        ans += 1
        ch_prev = ch
        
print(ans)