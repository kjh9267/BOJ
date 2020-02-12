# https://www.acmicpc.net/problem/1697


def bfs(start, target):
    queue = __import__('collections').deque()
    queue.append(start)

    visited = [-1 for _ in range(MAX)]
    visited[start] = 0

    while queue:
        cur = queue.popleft()
        for nxt in (cur - 1, cur + 1, cur * 2):
            if not (0 <= nxt < MAX):
                continue
            if visited[nxt] != -1:
                continue
            visited[nxt] = visited[cur] + 1
            queue.append(nxt)

    return visited[target]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    MAX = 100_001
    print(bfs(N, K))