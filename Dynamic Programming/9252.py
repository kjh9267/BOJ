# https://www.acmicpc.net/problem/9252

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

    result = list()
    a_index = N
    b_index = M
    while a_index != 0 and b_index != 0:
        if dp[a_index][b_index] == dp[a_index - 1][b_index]:
            a_index -= 1
        elif dp[a_index][b_index] == dp[a_index][b_index - 1]:
            b_index -= 1
        else:
            result.append(A[a_index - 1])
            a_index -= 1
            b_index -= 1


    print(dp[N][M])
    print(''.join(reversed(result)))