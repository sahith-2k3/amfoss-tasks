t = int(input())
for v in range(t):
    q = [int(i) for i in input().split()]
    A = 0
    S = 0
    A = [int(i) for i in input().split()]
    S = [int(i) for i in input().split()]
    n, m, k = q[0], q[1], q[2]
    res = 0
    curr_sum = 0
    k = min(k, m)
    for i in range(k):
        res += S[i]
    for i in range(k, len(A)):
        curr_sum += S[i] - S[i - k]
        res = max(res, curr_sum)
    if res >= n:
        print("YES")
    else:
        print("NO")
