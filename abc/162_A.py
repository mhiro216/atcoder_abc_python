n = int(input())

for i in range(3):
    if n % 10 == 7:
        print('Yes')
        break
    else:
        n //= 10
        continue
    break
else:
    print('No')