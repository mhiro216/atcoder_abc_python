import sys
sys.setrecursionlimit(10**6)

s = input()

l = [i for i in range(1,13)]
l = [str(i) if len(str(i))==2 else '0'+str(i) for i in l]

if s[:2] not in l and s[2:] not in l:
    print('NA')
elif s[:2] not in l and s[2:] in l:
    print('YYMM')
elif s[:2] in l and s[2:] not in l:
    print('MMYY')
else:
    print('AMBIGUOUS')