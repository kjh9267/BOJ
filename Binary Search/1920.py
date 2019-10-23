# https://www.acmicpc.net/problem/1920


def bs(num):
    lo = -1
    hi = N
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if nums[mid] == num:
            return 1
        if nums[mid] >= num:
            hi = mid
        else:
            lo = mid
    return 0


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    nums = list(sorted(map(int,input().split())))
    M = int(input())
    data = list(map(int,input().split()))

    for num in data:
        print(bs(num))