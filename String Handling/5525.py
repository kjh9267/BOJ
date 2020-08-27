# https://www.acmicpc.net/problem/5525


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    _i = 'I'
    _o = 'O'
    N = int(input())
    M = int(input())
    string = input().rstrip()
    result = 0
    cnt = 0
    idx = 0

    while idx < M - 2:
        if string[idx] == string[idx + 2] == _i and string[idx + 1] == _o:
            cnt += 1
            if cnt == N:
                result += 1
                cnt -= 1
            idx += 2
        else:
            cnt = 0
            idx += 1

    print(result)