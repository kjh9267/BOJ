#  https://www.acmicpc.net/problem/2108

input = __import__('sys').stdin.readline

t = int(input())
data = list()
nums = [[0,i - 4000] for i in range(8001)]
maxV = -4000
minV = 4000
sum = 0

for _ in range(t):
    n = int(input())
    data.append(n)
    if maxV < n:
        maxV = n
    if minV > n:
        minV = n
    nums[n + 4000][0] += 1
    sum += n

data = sorted(data)
nums = sorted(nums,key=lambda x:(x[0],x[1]))

temp = nums[8000][0]
cnt = 0
for i in range(8000,-1,-1):
    if nums[i][0] != temp:
        break
    cnt += 1

nums = sorted(nums[-cnt:],key=lambda x:x[1])

print(int(round(sum / t,0)))
print(data[t//2])
print(nums[1][1] if len(nums) > 1 else nums[0][1])
print(maxV - minV)