# https://www.acmicpc.net/problem/7453


def lower(num):
    lo = -1
    hi = limit
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if num + CD[mid] >= 0:
            hi = mid
        else:
            lo = mid
    return hi


def upper(num):
    lo = -1
    hi = limit
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if num + CD[mid] <= 0:
            lo = mid
        else:
            hi = mid
    return hi


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    limit = N ** 2
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    C = [0 for _ in range(N)]
    D = [0 for _ in range(N)]
    AB = list()
    CD = list()

    for i in range(N):
        A[i], B[i], C[i], D[i] = map(int,input().split())

    for i in range(N):
        for j in range(N):
            AB.append(A[i] + B[j])
            CD.append(C[i] + D[j])

    AB.sort()
    CD.sort()

    cnt = 0
    prev = 2 ** 30
    value = 0
    for num in AB:
        if prev == num:
            cnt += value
        else:
            value = upper(num) - lower(num)
            cnt += value
            prev = num

    print(cnt)