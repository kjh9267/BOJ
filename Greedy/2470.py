# https://www.acmicpc.net/problem/2470

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = list(sorted(map(int, input().split()), key=lambda x: abs(x)))
    minimum = float('inf')
    res = [0, 0]

    for idx in range(N - 1):
        diff = abs(data[idx] + data[idx + 1])
        if diff < minimum:
            minimum = diff
            res = [data[idx], data[idx + 1]]

    print(' '.join(map(str, sorted(res))))