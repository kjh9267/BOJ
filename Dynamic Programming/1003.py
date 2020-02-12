# https://www.acmicpc.net/problem/1003


def dfs(depth):
    if depth == 1:
        dp[1][1] = 1
        return dp[1]
    if depth == 0:
        dp[0][0] = 1
        return dp[0]
    if dp[depth] != [0, 0]:
        return dp[depth]
    dp[depth][0] = dfs(depth - 1)[0] + dfs(depth - 2)[0]
    dp[depth][1] = dfs(depth - 1)[1] + dfs(depth - 2)[1]
    return dp[depth]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dp = [[0, 0] for _ in range(41)]
    dfs(40)
    T = int(input())

    for _ in range(T):
        num = int(input())
        print(' '.join(map(str,dp[num])))