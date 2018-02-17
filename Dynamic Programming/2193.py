import sys

n = int(sys.stdin.readline())
dp = [[0 for j in range(2)] for i in range(n)]
dp[0][0] = 0
dp[0][1] = 1

for i in range(1,n):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n-1]))