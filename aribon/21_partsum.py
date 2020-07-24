## DFS 部分和問題

n = 4
a = [1,2,4,7]
k = 13

def dfs(i, sum):
    # n個決め終わったら、今までの和sumがkと等しいかを返す
    if i == n: return sum == k
    
    # a[i]を使わない場合
    if dfs(i+1, sum): return True
    
    # a[i]を使う場合
    if dfs(i+1, sum+a[i]): return True
    
    # a[i]を使う使わないに関わらずkが作れないのでfalseを返す
    return False

def partial_sum():
    if dfs(0, 0): return True
    else: return False
    
print(partial_sum())