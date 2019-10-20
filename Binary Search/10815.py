# https://www.acmicpc.net/problem/10815


def bs(num):
    lo = -1
    hi = N
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if A[mid] == num:
            return True
        if A[mid] > num:
            hi = mid
        else:
            lo = mid
    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    A = list(sorted(map(int, input().split())))
    M = int(input())
    B = list(map(int, input().split()))
    res = ''

    for num in B:
        res += '{} '.format(1 if bs(num) else 0)

    print(res)