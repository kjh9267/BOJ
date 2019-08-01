# https://www.acmicpc.net/problem/9019


def bfs(A, B):
    queue = __import__('collections').deque()
    queue.append((A, list()))
    visited = [False for _ in range(10000)]
    visited[A] = True
    while queue:
        cur, move = queue.popleft()
        nxt = (cur * 2) % 10000
        if not visited[nxt]:
            if nxt == B:
                return move + ['D']
            visited[nxt] = True
            queue.append((nxt, move + ['D']))
        nxt = cur - 1 if cur != 0 else 9999
        if not visited[nxt]:
            if nxt == B:
                return move + ['S']
            visited[nxt] = True
            queue.append((nxt, move + ['S']))
        nxt = (cur % 1000) * 10 + cur // 1000
        if not visited[nxt]:
            if nxt == B:
                return move + ['L']
            visited[nxt] = True
            queue.append((nxt, move + ['L']))
        nxt = (cur // 10) + (cur % 10) * 1000
        if not visited[nxt]:
            if nxt == B:
                return move + ['R']
            visited[nxt] = True
            queue.append((nxt, move + ['R']))
    return ''


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    T = int(input())

    for _ in range(T):
        A, B = map(int,input().split())
        print(''.join(bfs(A, B)))