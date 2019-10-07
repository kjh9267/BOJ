if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    N, M = map(int,input().split())

    grid = [list(map(int,input().split())) for _ in range(N)]

    r1, c1, r2, c2 = 0, 0, 0, 0

    key = False
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                r1 = i
                c1 = j
                grid[i][j] = 0
                key=True
                break
        if key:
            break

    key = False
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                r2 = i
                c2 = j
                key = True
                break
        if key:
            break

    print(abs(r1 - r2) + abs(c1 - c2))