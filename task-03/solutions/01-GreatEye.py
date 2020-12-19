t = int(input())
for i in range(t):
    k = int(input())
    list = [i for i in input().split()]
    if len(list) > k:
        sum = 0
        for i in list[k]:
            sum += ord(i)
        print(sum)
    else:
        print(-1)
