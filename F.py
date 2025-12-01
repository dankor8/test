def verif(n1, k1):
    ans = 1
    for a in range(1, n1 + 1):
        if a <= n1 - k1 and a <= k1:
            ans /= a
        if a > n1 - k1 and a > k1:
            ans *= a
    return ans
z = int(input())
n = z - 1
k = 0
while True:
    n += 1
    k = 0
    while k < n and k < z:
        k += 1
        v = verif(n, k)
        if v > z:
            break
        if v == z:
            print(n)
            exit()