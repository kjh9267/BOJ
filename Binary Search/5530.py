# https://www.acmicpc.net/problem/5530


def bs():
    lo = 0
    hi = limit
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    return lo


def check(cnt):
    first, second, third = 0, 0, 0
    if not i_idx:
        return False
    end = i_idx[len(i_idx) - cnt]
    for idx, value in enumerate(data):
        if value == 'I' and idx >= end and second > third:
            third += 1
        elif value == 'J' or value == 'I':
            first += 1
        elif value == 'O' and first > second:
            second += 1
    return third >= cnt


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = list(input().rstrip())
    limit = N // 3 + 1
    i_idx = list()

    for idx, value in enumerate(data):
        if value == 'I':
            i_idx.append(idx)

    print(bs())