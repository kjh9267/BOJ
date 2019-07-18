# https://www.acmicpc.net/problem/17253


def solve(N):
    if N == 0:
        return 'NO'
    visited = set()
    while N > 0:
        x = 1
        cnt = 0
        while x <= N:
            x *= 3
            cnt += 1
        cnt -= 1
        if cnt in visited:
            return 'NO'
        visited.add(cnt)
        N -= x // 3
    return 'YES'


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    print(solve(N))