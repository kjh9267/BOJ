# https://www.acmicpc.net/problem/1874

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    target = [int(input()) for _ in range(N)]
    stack = list()
    res = list()
    pointer = 0

    for idx in range(1, N + 1):
        stack.append(idx)
        res.append('+')
        while stack and stack[-1] == target[pointer]:
            stack.pop()
            res.append('-')
            pointer += 1

    if stack:
        print('NO')
    else:
        print('\n'.join(res))
