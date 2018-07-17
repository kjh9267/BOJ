import sys

res = []

for string in sys.stdin:
    string = string.split()
    res += [j for i in string for j in i]

res = list(map(lambda x:ord(x) - 97,res))
nums = [0 for _ in range(26)]

for i in res:
    nums[i] += 1

maximum = max(nums)
result = ''

for i, j in enumerate(nums):
    if j == maximum:
        result += chr(i+97)

print(result)