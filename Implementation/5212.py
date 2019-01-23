#  지구 온난화
#  https://www.acmicpc.net/problem/5212


def find():
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 'X' and check(c, r) >= 3:
                targets.append((c, r))
    for c, r in targets:
        graph[r][c] = '.'


def check(x, y):
    cnt = 0
    for i, j in zip(dx, dy):
        xx = x + i
        yy = y + j
        if not (0 <= xx < C and 0 <= yy < R):
            cnt += 1
        elif graph[yy][xx] == '.':
            cnt += 1
    return cnt


def remove_water():
    x1, x2, y1, y2 = 0, 0, 0, 0

    for index, row in enumerate(graph):
        if 'X' in row:
            y1 += index
            break

    for index in range(R - 1, -1, -1):
        if 'X' in graph[index]:
            y2 += index
            break

    key = False
    for c in range(C):
        for r in range(R):
            if graph[r][c] == 'X':
                x1 += c
                key = True
                break
        if key is True:
            break

    key = False
    for c in range(C - 1, -1, -1):
        for r in range(R):
            if graph[r][c] == 'X':
                x2 += c
                key = True
                break
        if key is True:
            break
    return x1, x2, y1, y2


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    R, C = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(R)]
    targets = list()

    find()
    x1, x2, y1, y2 = remove_water()

    for row in graph[y1:y2+1]:
        print(''.join(row[x1:x2+1]))
