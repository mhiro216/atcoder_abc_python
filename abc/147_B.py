s = input()

if len(s)%2 == 0:
    mid = len(s)//2
    s_first = s[:mid]
    s_last = s[mid:]
else:
    mid = len(s)//2
    s_first = s[:mid]
    s_last = s[(mid+1):]
    
ans = 0
for i,j in zip(s_first, s_last[::-1]):
    if i!= j:
        ans += 1
        
print(ans)