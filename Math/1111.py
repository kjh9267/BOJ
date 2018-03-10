import sys

n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
length = len(nums)

if length is 1:
    print('A')
elif length is 2:
    if nums[0] == nums[1]:
        print(nums[1])
    else:
        print('A')
else:
    a = nums[-1] // nums[-2]
    b = nums[-1] % nums[-2]
    temp = (a, b)
    for i in range(length-1,0,-1):
        print(a, b)
        a = nums[i] // nums[i-1]
        b = nums[i] % nums[i-1]
        if (a, b) != temp:
            print('B')
            exit()
        temp = (a, b)
    print(a * nums[-1] + b)