z = []
for i in range(100,1000):
        for j in range(100,1000):
            a = i*j
            if str(a) == str(a)[::-1]:
                z.append(a)
z.sort()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())    
    ans = 0

    for i in z:
        if i < n:
            ans = i
        else:
            break
    print(ans)
