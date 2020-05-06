import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
A = [[int(i) for i in readline().split()] for _ in range(3)]
n = int(readline())
b = [int(readline()) for _ in range(n)]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            A[i][j] = 0
        
if A[0][0]+A[1][1]+A[2][2] == 0 \
or A[0][2]+A[1][1]+A[2][0] == 0 \
or A[0][0]+A[0][1]+A[0][2] == 0 \
or A[1][0]+A[1][1]+A[1][2] == 0 \
or A[2][0]+A[2][1]+A[2][2] == 0 \
or A[0][0]+A[1][0]+A[2][0] == 0 \
or A[0][1]+A[1][1]+A[2][1] == 0 \
or A[0][2]+A[1][2]+A[2][2] == 0 :
    print('Yes')
else:
    print('No')