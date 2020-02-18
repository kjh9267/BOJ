# https://www.acmicpc.net/problem/2239

# https://www.acmicpc.net/problem/2580


def init():
    for row in range(N):
        for col in range(N):
            if data[row][col] == 0:
                continue
            row_sets[row].add(data[row][col])

    for col in range(N):
        for row in range(N):
            if data[row][col] == 0:
                continue
            col_sets[col].add(data[row][col])

    for row in range(N):
        r = row // 3
        for col in range(N):
            if data[row][col] == 0:
                continue
            c = col // 3
            mid_sets[r * 3 + c].add(data[row][col])


def dfs(depth):
    if depth == 81:
        return True
    y = depth // N
    x = depth % N

    if data[y][x] != 0:
        if dfs(depth + 1):
            return True
        return False

    for num in range(1, 10):
        if can_go(y, x, num):
            visited(True, num, y, x)
            if dfs(depth + 1):
                return True
            visited(False, num, y, x)

    return False


def can_go(row, col, num):
    if num in row_sets[row]:
        return False
    if num in col_sets[col]:
        return False
    if num in mid_sets[(row // 3) * 3 + (col // 3)]:
        return False
    return True


def visited(insert, num, row, col):
    if insert:
        data[row][col] = num
        row_sets[row].add(num)
        col_sets[col].add(num)
        mid_sets[(row // 3) * 3 + (col // 3)].add(num)
    else:
        data[row][col] = 0
        row_sets[row].remove(num)
        col_sets[col].remove(num)
        mid_sets[(row // 3) * 3 + (col // 3)].remove(num)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = 9
    data = [list(map(int,input().rstrip())) for _ in range(N)]
    row_sets = [set() for _ in range(N)]
    col_sets = [set() for _ in range(N)]
    mid_sets = [set() for _ in range(N)]

    init()
    dfs(0)

    for line in data:
        print(''.join(map(str, line)))
