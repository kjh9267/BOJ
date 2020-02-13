# https://www.acmicpc.net/problem/13913


def bfs(start, target):
    queue = __import__('collections').deque()
    queue.append(start)
    visited = [-1 for _ in range(MAX)]
    visited[start] = 0
    way = [-1 for _ in range(MAX)]

    while queue:
        cur = queue.popleft()
        for nxt in (cur - 1, cur + 1, cur * 2):
            if not (0 <= nxt < MAX):
                continue
            if visited[nxt] != -1:
                continue
            visited[nxt] = visited[cur] + 1
            way[nxt] = cur
            queue.append(nxt)

    return '{}\n{}'.format(visited[target], find_path(way))


def find_path(way):
    cur = K
    res = __import__('collections').deque()
    res.append(K)
    while cur != N:
        res.appendleft(way[cur])
        cur = way[cur]
    return ' '.join(map(str, res))


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    MAX = 100_001
    _space = ' '
    N, K = map(int,input().split())
    print(bfs(N, K))