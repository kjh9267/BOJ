# https://www.acmicpc.net/problem/11866

from collections import deque

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    queue = deque(map(lambda x: x + 1, range(N)))
    result = list()

    for _ in range(N):
        for _ in range(K):
            queue.append(queue.popleft())
        result.append(queue.pop())

    print('<{}>'.format(', '.join(map(str, result))))