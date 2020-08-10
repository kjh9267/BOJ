# https://www.acmicpc.net/problem/6603


def dfs(cur, depth, nums):
    if depth == _target:
        result.append(nums)
        return
    for idx in range(cur, K):
        dfs(idx + 1, depth + 1, nums + [data[idx]])


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _target = 6
    result = list()

    while True:
        data = list(map(int, input().split()))
        K = data[0]
        data = data[1:]

        if K == 0:
            break

        dfs(0, 0, list())

        for value in result:
            print(' '.join(map(str, value)))

        print()
        result.clear()
