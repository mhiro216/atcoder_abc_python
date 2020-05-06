h = int(input())

ans = 0
x = 0

def dfs(h,x):
    global ans
    if h == 1:
        ans += 2**x
        return
    else:
        ans += 2**x
        h //= 2
        x += 1
        dfs(h, x)
        
dfs(h,x)

print(ans)