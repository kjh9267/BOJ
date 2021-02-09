# https://www.acmicpc.net/problem/20437
from sys import stdin
from collections import deque

if __name__ == '__main__':
    input = stdin.readline
    inf = float('inf')
    new_line = '\n'
    no_answer = '-1'
    T = int(input())
    result = deque()

    for _ in range(T):
        string = input().rstrip()
        K = int(input())
        indexes = [list() for _ in range(26)]
        min_size = inf
        max_size = -1

        for index, character in enumerate(string):
            indexes[ord(character) - 97].append(index)

        for character in range(26):
            for idx in range(K - 1, len(indexes[character])):
                size = indexes[character][idx] - indexes[character][idx - K + 1] + 1
                min_size = min(min_size, size)
                max_size = max(max_size, size)

        if min_size == inf:
            result.append(no_answer)
        else:
            result.append('{} {}'.format(min_size, max_size))

    print(new_line.join(result))