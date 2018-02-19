import sys

n = int(sys.stdin.readline())

dp = [[0 for j in range(10)] for i in range(n)]

for i in range(10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        for u in range(j+1):
            dp[i][j] += dp[i-1][u]

print(sum(dp[n-1])%10007)