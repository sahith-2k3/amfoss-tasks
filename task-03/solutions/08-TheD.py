n = int(input())
z = int(n//2)
#first half

for i in range(z):
    y = '*' * (z-i)
    x = 'D' * (2*i+1)
    print(y+x+y)

#mid line
x = 'D' * n
print(x)


#second half
for i in range(z):
    y = '*' * (i+1)
    x = 'D' * (2*(z-i-1)+1)
    print(y+x+y)
