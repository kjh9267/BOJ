import sys

nums = [int(sys.stdin.readline()) for _ in range(9)]
add = sum(nums)

for i, j in enumerate(nums):
    for o, p in enumerate(nums):
        if i is o:
            continue
        if add - j - p == 100:
            nums.remove(j)
            nums.remove(p)
            for u in sorted(nums):
                print(u)
            exit()