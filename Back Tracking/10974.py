# https://www.acmicpc.net/problem/10974


def dfs(depth, nums):
    if depth == N:
        res.append(nums)
    for idx in range(N):
        if visited[idx]:
            continue
        visited[idx] = True
        dfs(depth + 1, nums + '{} '.format(data[idx]))
        visited[idx] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    res = list()
    data = list(range(1, N + 1))
    visited = [False for _ in range(N)]
    dfs(0, '')
    for r in res:
        print(r)