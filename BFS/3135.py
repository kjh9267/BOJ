# https://www.acmicpc.net/problem/3135


def bfs():
    queue = __import__('collections').deque()
    queue.append(A)
    queue.extend(data)
    visited = [-1 for _ in range(1000)]
    for ch in data:
        visited[ch] = 1
    visited[A] = 0

    while queue:
        cur = queue.popleft()
        for diff in range(-1, 2, 2):
            nxt = cur + diff
            if not (1 <= nxt <= 999):
                continue
            if visited[nxt] != -1:
                continue
            queue.append(nxt)
            visited[nxt] = visited[cur] + 1
    return visited[B]


if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    data = list()
    A, B = map(int,input().split())
    N = int(input())

    for _ in range(N):
        data.append(int(input()))

    if B in data:
        print(1)
    else:
        print(bfs())