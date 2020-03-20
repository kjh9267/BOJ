# https://www.acmicpc.net/problem/15988


def init():
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for num in range(4, MAX + 1):
        for diff in range(1, 4):
            dp[num] = ((dp[num] % MOD) + (dp[num - diff] % MOD)) % MOD


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    MAX = 1_000_000
    MOD = 1_000_000_009

    T = int(input())
    dp = [0 for _ in range(MAX + 1)]
    init()

    for _ in range(T):
        N = int(input())
        print(dp[N])