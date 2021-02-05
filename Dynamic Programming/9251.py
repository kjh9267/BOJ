# https://www.acmicpc.net/problem/9251

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    A = input().rstrip()
    B = input().rstrip()
    N = len(A)
    M = len(B)
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for a_index, a_char in enumerate(A):
        for b_index, b_char in enumerate(B):
            if b_char == a_char:
                dp[a_index + 1][b_index + 1] = dp[a_index][b_index] + 1
            else:
                dp[a_index + 1][b_index + 1] = max(dp[a_index][b_index + 1],
                                                   dp[a_index + 1][b_index])

    print(dp[N][M])