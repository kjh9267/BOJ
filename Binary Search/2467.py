# https://www.acmicpc.net/problem/2467


def binary_search(lo):
    hi = N
    value = data[lo]

    while lo + 1 < hi:
        mid = (lo + hi) >> 1

        if abs(value + data[mid]) < abs(result[0] + result[1]):
            result[0] = value
            result[1] = data[mid]

        if value + data[mid] <= 0:
            lo = mid
        else:
            hi = mid

    return lo


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = list(map(int, input().split()))
    result = [float('inf'), float('inf')]

    for idx in range(N):
        binary_search(idx)

    print(' '.join(map(str, sorted(result))))