"""
第三の条件「隣接する 2 文字の入れ替えを 1 回行うことで第二の条件 (部分文字列として AGC を含まない)
に違反させることはできない」を言い換えると、「部分文字列として GAC, ACG, A?GC, AG?C のいずれも含まな
い (? は何らかの 1 文字)」となります。
よって、条件を満たす文字列を 1 文字目から順に作るとき、「i 文字目を何にするか」の選択は、「i − 4 文字
目以前が何であったか」を気にすることなく、i−3, i−2, i−1 文字目のみを考慮して行うことができます。こ
れを元に、メモ化再帰または動的計画法により N の線形時間で解を求められます (“定数倍” は大きいです)。
"""


import sys
sys.setrecursionlimit(10**6)

N = int(input())
MOD = 10**9+7
memo = [{} for i in range(N+1)] # (文字数N, 最後3文字の文字列)の組み合わせについて場合の数を覚えていく

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i-1], t[i] = t[i], t[i-1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True

def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0
    for c in 'ACGT':
        if ok(last3 + c):
            ret = (ret + dfs(cur+1, last3[1:]+c)) % MOD
            memo[cur][last3] = ret
    return ret

print(dfs(0, 'TTT'))