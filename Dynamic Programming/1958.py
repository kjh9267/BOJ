# https://www.acmicpc.net/problem/1958

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    A = input().rstrip()
    B = input().rstrip()
    C = input().rstrip()
    N = len(A)
    M = len(B)
    L = len(C)

    dp = [[[0 for _ in range(L + 1)] for _ in range(M + 1)] for _ in range(N + 1)]

    for a_index, a_char in enumerate(A):
        for b_index, b_char in enumerate(B):
            for c_index, c_char in enumerate(C):
                if b_char == a_char == c_char:
                    dp[a_index + 1][b_index + 1][c_index + 1] = dp[a_index][b_index][c_index] + 1
                else:
                    dp[a_index + 1][b_index + 1][c_index + 1] = max(dp[a_index][b_index + 1][c_index + 1],
                                                                    dp[a_index + 1][b_index][c_index + 1],
                                                                    dp[a_index + 1][b_index + 1][c_index])

    print(dp[N][M][L])