#  https://www.acmicpc.net/problem/16940


def bfs():
    cnt = 1
    pointer = 1
    visited[1] = True
    queue.append(1)
    while queue:
        cur = queue.popleft()
        while pointer != N:
            if visited[res[pointer]]:
                continue
            if parent[res[pointer]] != cur:
                break
            cnt += 1
            visited[res[pointer]] = True
            queue.append(res[pointer])
            pointer += 1
    if cnt == N:
        return 1
    return 0


def parent_init():
    queue = __import__('collections').deque()
    queue.append(1)
    visited[1] = True
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            parent[nxt] = cur
            visited[nxt] = True
            queue.append(nxt)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N = int(input())
    graph = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]

    for _ in range(N - 1):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    res = list(map(int, input().split()))
    queue = __import__('collections').deque()

    if res[0] != 1:
        print(0)
        exit()

    parent_init()
    visited = [False for _ in range(N + 1)]
    print(bfs())
