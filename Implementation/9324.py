# https://www.acmicpc.net/problem/9324


def solve():
    counts = [0 for _ in range(26)]
    for idx, char in enumerate(M):
        atoi = ord(char) - 65
        counts[atoi] += 1
        if counts[atoi] == 3:
            if idx == len(M) - 1 or M[idx + 1] != char:
                return 'FAKE'
            else:
                counts[atoi] = -1
    return 'OK'


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    t = int(input())
    for _ in range(t):
        M = input().rstrip()
        print(solve())