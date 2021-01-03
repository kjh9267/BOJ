# https://www.acmicpc.net/problem/11441

from sys import stdin
from collections import deque

if __name__ == '__main__':
    input = stdin.readline
    new_line = '\n'
    N = int(input())
    data = list(map(int, input().split()))
    dp = [0 for _ in range(N + 1)]
    dp[1] = data[0]

    for idx in range(1, N + 1):
        dp[idx] = data[idx - 1] + dp[idx - 1]

    result = deque()
    for _ in range(int(input())):
        i, j = map(int, input().split())
        result.append(dp[j] - dp[i - 1])

    print('{}'.format(new_line).join(map(str,result)))