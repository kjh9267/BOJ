#  https://www.acmicpc.net/problem/15873

input = __import__('sys').stdin.readline

nums = input().rstrip()
size = len(nums)
a = 0
b = 0

if size == 3:
    if nums[1] == '0':
        a = int(nums[:2])
        b = int(nums[-1])
    else:
        a = int(nums[:1])
        b = int(nums[-2:])
else:
    a = int(nums[:size//2])
    b = int(nums[size//2:])

print(a + b)