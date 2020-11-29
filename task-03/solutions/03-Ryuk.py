n = int(input())
w = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
for i in range(n):
    x[i] = x[i] // w[i]
print(min(x))
