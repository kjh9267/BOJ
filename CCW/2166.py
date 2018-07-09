import sys

n = int(sys.stdin.readline())
points = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
res = 0

for i in range(n-1):
    res += points[i][0]*points[i+1][1] - points[i][1]*points[i+1][0]

res += points[n-1][0]*points[0][1] - points[n-1][1]*points[0][0]

print(round(abs(res/2),2))