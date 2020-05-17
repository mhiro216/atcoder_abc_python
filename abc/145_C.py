"""順列"""

n = int(input())

xy = []
for i in range(n):
    x,y = map(int, input().split())
    xy.append((x,y))

from itertools import permutations

node = [i for i in range(n)]
node_perms = list(permutations(node))

d_list = []
for node in node_perms:
    d = 0
    for i in range(len(node)-1):
        n1 = node[i]
        n2 = node[i+1]
        tmp = ((xy[n1][0]-xy[n2][0])**2+(xy[n1][1]-xy[n2][1])**2)**(1/2)
        d += tmp
    d_list.append(d)

print(sum(d_list)/len(d_list))