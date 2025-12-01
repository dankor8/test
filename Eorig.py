from os.path import abspath
def find(n, m):
    if n == 0:
        return [[]]
    nfps = []
    for i in range(1, min(n, m) + 1):
        for p in find(n - i, i):
            nfps.append(p + [i])
    return nfps
anses = {}
for num in range(1, 31):
    ps = [sorted(x) for x in sorted(find(num, num))]
    for s in range(1, num + 1):
        anses[(num, s)] = [x for x in ps if sum([sum(list(map(int, str(y)))) for y in x]) == s]
    print(num)
with open('summa_tsyfr.py', 'w') as f:
    f.write(f'mas = [" ".join(list(map(str, x))) for x in {str(anses)}[tuple(map(int, input().split()))]]\nprint(len(mas), *mas, sep="\\n")')
print(abspath('anses.txt'))