# https://www.acmicpc.net/problem/1010

from math import factorial


def combination(a,b):
    f = factorial
    return f(a) // f(a - b) // f(b)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(combination(M, N))