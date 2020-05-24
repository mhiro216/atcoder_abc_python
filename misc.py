def get_divisors(n):
    """約数の列挙"""
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: # NNが平方数のときに√Nを2個出力しないようにする
                divisors.append(n//i)

    # divisors.sort()
    return divisors