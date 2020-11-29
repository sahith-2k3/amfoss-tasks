t = int(input())
for i in range(t):
    y = int(input())
    z = [item for item in str(input()).split()]
    sum = 0
    if y <= len(z):
        for x in z[y]:
            sum += ord(x)
        print(sum)
    elif y > len(z):
        print(-1)
