# https://www.acmicpc.net/problem/12851


def bfs(start, target):
    queue = __import__('collections').deque()
    queue.append(start)
    visited = [False for _ in range(MAX)]
    mini = 0
    cnt = 0
    end = False

    while queue:
        size = len(queue)
        mini += 1

        for _ in range(size):
            cur = queue.popleft()
            visited[cur] = True
            for nxt in (cur - 1, cur + 1, cur * 2):
                if not (0 <= nxt < MAX):
                    continue
                if visited[nxt]:
                    continue
                if nxt == target:
                    end = True
                    cnt += 1
                queue.append(nxt)
        if end:
            return '\n'.join(map(str, (mini , cnt)))

    return -1


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    MAX = 100_001

    if N == K:
        print('0\n1')
    else:
        print(bfs(N, K))