n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = input()

ctoi = {'r':2, 'c':0, 'p':1}

ans = 0



def main():
    N, K = [int(i) for i in input().split()]
    R, S, P = [int(i) for i in input().split()]
    T = input()
    hand = {"r":P, "s":R, "p":S}
    res = 0
    for i in range(K):
        # print(K)
        last = ""
        j = i
        while j < N:
            # print(j)
            aite = T[j]
            if aite != last:
                res += hand[aite]
                last = aite
            else:
                last=""
            j += K
    print(res)
main()

