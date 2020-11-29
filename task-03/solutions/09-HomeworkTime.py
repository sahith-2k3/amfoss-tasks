t = int(input())
def rev(n):
    rn = 0
    while(n):
        x = n % 10
        rn = rn* 10 + x
        n //= 10
    return rn
r = []
for i in range(t):
    ri = int(input())
    r.append(ri)
b = max(r)
dp = [0] * (b+1)
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, b+1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for i in range(t):
    print(rev(dp[r[i]]))
