t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    m = str(n)
    a = len(m)
    z = a - k + 1
    nsl = []
    mnsl = []
    for y in range(z):
        x = 0
        for j in range(k):
            x += int(m[y + j])
        nsl.append(x)
    for i in range(len(nsl)-1):
        x = abs(nsl[i] - nsl[i+1])
        mnsl.append(x)
    if not mnsl:
        print('-1')
    else:
        print(min(mnsl))
