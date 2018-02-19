import sys

n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
fish = [0]
dp = [0]*(n+1)

for i in p:
    fish.append(i)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + fish[j])

print(dp[n])