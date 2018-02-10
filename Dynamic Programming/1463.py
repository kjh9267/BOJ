import sys

n = int(sys.stdin.readline())
inf = float('inf')
dp = [inf for _ in range(n+1)]
dp[1] = 0

for i in range(1,n+1):
    if i+1 <= n and dp[i+1] > dp[i] + 1:
        dp[i+1] = dp[i] + 1
    if i*2 <= n and dp[i*2] > dp[i] + 1:
        dp[i*2] = dp[i] + 1
    if i*3 <= n and dp[i*3] > dp[i] + 1:
        dp[i*3] = dp[i] + 1

print(dp[n])