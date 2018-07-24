import sys

n = int(sys.stdin.readline())
graph = list(map(int,sys.stdin.readline().split()))
inf = float('inf')
dp = [inf for _ in range(n)]
dp[0] = 0

for i in range(n):
    for j in range(1,graph[i]+1):
        if i + j < n and dp[i + j] > dp[i] + 1:
            dp[i + j] = dp[i] + 1

if dp[-1] is inf:
    print(-1)
else:
    print(dp[-1])