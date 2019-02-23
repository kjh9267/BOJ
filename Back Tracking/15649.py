#  https://www.acmicpc.net/problem/15649


def dfs(cur, depth, string):
    if depth == M:
        res.append(string)
        return
    if cur == N:
        return
    for index in range(0, N):
        if visited[index]:
            continue
        visited[index] = True
        dfs(index, depth + 1, string + nums[index] + ' ')
        visited[index] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int, input().split())
    nums = list(map(str, range(1, N + 1)))
    visited = [False for _ in range(N)]
    res = list()
    dfs(0, 0, '')
    print('\n'.join(res))
