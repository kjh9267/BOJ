# https://www.acmicpc.net/problem/17828

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, X = map(int, input().split())
    res = __import__('collections').deque()

    if N * 26 < X or N > X:
        print('!')
        exit()

    for As in range(N - 1, -1, -1):
        value = min(X - As, 26)
        res.appendleft(value)
        X -= value

    print(''.join(map(lambda x: chr(x + 64), res)))
