import sys


def dfs(cur):
    if cur == k:
        return

    if len(selected + [nums[cur]]) == 6:
        res.append(selected + [nums[cur]])

    selected.append(nums[cur])
    dfs(cur+1)
    selected.pop()
    dfs(cur+1)


cnt = 0
while True:
    if cnt != 0:
        print()

    nums = list(map(int,sys.stdin.readline().split()))

    if nums == [0]:
        break

    k = nums[0]
    nums = nums[1:]
    selected = []
    res = []

    dfs(0)

    for i in res:
        print(" ".join(map(str,i)))

    cnt += 1