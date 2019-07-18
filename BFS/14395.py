# https://www.acmicpc.net/problem/14395


def bfs():
    queue = __import__('collections').deque()
    queue.append((S, list()))
    visited = set()
    visited.add(S)
    while queue:
        cur = queue.popleft()
        if cur[0] == T:
            res.append(cur[1])
            return True
        nxt = cur[0] ** 2
        if nxt not in visited and nxt <= T:
            queue.append((nxt, cur[1] + ['*']))
            visited.add(nxt)
        nxt = cur[0] * 2
        if nxt not in visited and nxt <= T:
            queue.append((nxt, cur[1] + ['+']))
            visited.add(nxt)
        nxt = 1
        if nxt not in visited and nxt <= T:
            queue.append((nxt, cur[1] + ['/']))
            visited.add(nxt)
    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    S, T = map(int,input().split())
    res = list()

    if S == T:
        print(0)
    elif T == 1 and S != 1:
        print('/')
    else:
        if bfs():
            print(''.join(res[0]))
        else:
            print(-1)
