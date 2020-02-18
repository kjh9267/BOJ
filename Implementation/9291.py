# https://www.acmicpc.net/problem/9291


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


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = 9
    target = [set(range(1, 10)) for _ in range(9)]
    T = int(input())

    for i in range(T):
        data = [list(map(int, input().split())) for _ in range(N)]
        row_sets = [set() for _ in range(N)]
        col_sets = [set() for _ in range(N)]
        mid_sets = [set() for _ in range(N)]
        init()

        if target == row_sets == col_sets == mid_sets:
            print("Case {}: {}".format(i + 1, 'CORRECT'))
        else:
            print("Case {}: {}".format(i + 1, 'INCORRECT'))

        input()
