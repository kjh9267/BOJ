import sys

n, k = map(int,sys.stdin.readline().split())
coin = [0]*n
inf = float('inf')
dp = [inf]*10001

for i in range(n):
    a = int(sys.stdin.readline())
    if a <= 10000:
        dp[a] = 1
        coin[i] = a

for i in range(1,k+1):
    for j in coin:
        dp[i] = min(dp[i], dp[i-j] + 1)

if dp[k] == inf:
    print(-1)
else:
    print(dp[k])