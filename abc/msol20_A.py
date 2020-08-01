import sys
sys.setrecursionlimit(10**6)

x = int(input())s

if 400 <= x <= 599:
    print('8')
if 600 <= x <= 799:
    print('7')
if 800 <= x <= 999:
    print('6')
if 1000 <= x <= 1199:
    print('5')
if 1200 <= x <= 1399:
    print('4')
if 1400 <= x <= 1599:
    print('3')
if 1600 <= x <= 1799:
    print('2')
if 1800 <= x <= 1999:
    print('1')