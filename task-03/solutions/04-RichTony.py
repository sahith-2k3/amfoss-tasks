t = int(input())
for i in range(t):
    z = [int(i) for i in input().split()]
    n, k = z[0], z[1]
    x = [int(i) for i in input().split()]
    result = 1
    for i in range(n):
        result *= x[i]
    lsit = []
    for i in range(n):
        y = result / x[i] * (x[i] - k)
        lsit.append(int(y))
    print(max(lsit))
