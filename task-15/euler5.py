t = int(input())
for i in range(t):
    n = int(input())
    prime = []
    for i in range(2, n+1):
        fac = []
        for j in range(2, i):
            if i % j == 0:
                fac.append(j)
        if not fac:
            prime.append(i)
    ans = 1
    for i in prime:
        z = i
        while i<=n:
            i*=z
        ans *= i // z
    print(ans)
