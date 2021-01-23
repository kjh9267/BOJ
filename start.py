def dfs(cur):
    if cur == 1:
        return 4
    if cur == 2:
        return 6
    if dp[cur] != 0:
        return dp[cur]

    dp[cur] = dfs(cur - 1) + dfs(cur - 2)

    return dp[cur]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    __import__('sys').setrecursionlimit(999999999)
    N = int(input())
    dp = [0 for _ in range(N + 1)]
    print(dfs(N))