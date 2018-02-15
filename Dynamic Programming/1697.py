import sys

n, k = map(int,sys.stdin.readline().split())
dp = [0 for _ in range(100001)]
dp[n] = 0
cnt = 1

if n == k:
    print(0)
else:
    for i in range(n-1,-1,-1):
        dp[i] = cnt
        cnt += 1
    for i in range(n+1,100001):
        if i % 2 == 0:
            dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)
        else:
            dp[i] = min(dp[i-1] + 1, dp[(i+1)//2] + 2)
    print(dp[k])