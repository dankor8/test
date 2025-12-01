s = input()
n = len(s)
total = n * (n + 1) // 2
sc = 0
currLenin = 1
for i in range(1, n):
    if s[i] == s[i - 1]:
        currLenin += 1
        continue
    sc += currLenin * (currLenin + 1) // 2
    currLenin = 1
sc += currLenin * (currLenin + 1) // 2
print(total - sc)