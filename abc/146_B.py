"""アルファベット"""

n = int(input())
s = input()

al = [chr(ord('A') + i) for i in range(26)]
ans = ''

for ch in s:
    idx = (ord(ch)+n-ord('A'))%26
    ans += al[idx]
    
print(ans)