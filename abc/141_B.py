s = input()

l_odd = ['R', 'U', 'D']
l_even = ['L', 'U', 'D'] 

for i, ch in enumerate(s):
    if (i+1)%2 != 0 and ch not in l_odd:
        print('No')
        break
    if (i+1)%2 == 0 and ch not in l_even:
        print('No')
        break
else:
    print('Yes')