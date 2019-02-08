#  https://www.acmicpc.net/problem/8112


def bfs(num):
    queue = __import__('collections').deque()
    queue.append(1)
    visited = [False for _ in range(1000001)]
    visited[1] = True

    while queue:
        cur = queue.popleft()
        # print(cur)
        mod = cur % num
        if mod == 0:
            return cur
        else:
            if not visited[(cur * 10) % N]:
                visited[(cur * 10) % N] = True
                queue.append(cur * 10)
            if not visited[(cur * 10 + 1) % N]:
                visited[(cur * 10 + 1) % N] = True
                queue.append(cur * 10 + 1)
    return 'BRAK'


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    T = int(input())

    for _ in range(T):
        N = int(input())
        print(bfs(N))
