# https://www.acmicpc.net/problem/13549


def bfs(start, target):
    queue = __import__('collections').deque()
    queue.append(start)

    visited = [-1 for _ in range(MAX)]
    visited[start] = 0

    while queue:
        cur = queue.popleft()
        for idx, nxt in enumerate((cur * 2, cur - 1, cur + 1)):
            if not (0 <= nxt < MAX):
                continue
            if visited[nxt] != -1:
                continue
            visited[nxt] = visited[cur] + (1 if idx > 0 else 0)
            queue.append(nxt)

    return visited[target]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    MAX = 100_001
    N, K = map(int,input().split())
    print(bfs(N, K))