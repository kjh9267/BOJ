import sys

a, b, n, m = map(int,sys.stdin.readline().split())
inf = float('inf')
dp = [inf for _ in range(100001)]
dp[n] = 0

for i in range(n,-1,-1):
    if i + a < 100001:
        dp[i] = dp[i+a]
    if i + b < 100001:
        dp[i] = dp[i+b]
    if i // a