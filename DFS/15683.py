#  https://www.acmicpc.net/problem/15683


class TV:
    @classmethod
    def turn(cls, a, b):
        return a + b if a + b <= 3 else a + b - 4

    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

    def get_dir(self, case):
        if self.num == 1:
            return [case]
        elif self.num == 2:
            return [case, TV.turn(case, 2)]
        elif self.num == 3:
            return [case, TV.turn(case, 1)]
        elif self.num == 4:
            return [case, TV.turn(case, 1), TV.turn(case, 2)]
        else:
            return [0, 1, 2, 3]


def init():
    for row in range(N):
        for col in range(M):
            value = graph[row][col]
            if value != 0 and value != 6:
                tvs.append(TV(col,row,value))


def dfs(cur, cases):
    global res
    if cur == len(tvs):
        see(cases)
        return
    for case in range(4):
        cases[cur] = case
        dfs(cur + 1, cases)


def check(temp):
    cnt = 0
    for row in range(N):
        for col in range(M):
            if temp[row][col] == 0:
                cnt += 1
    return res if res < cnt else cnt


def see(cases):
    global res
    temp = deep_copy()
    for index, case in enumerate(cases):
        dirs = tvs[index].get_dir(case)
        x, y = tvs[index].x, tvs[index].y
        temp[y][x] = 7
        for i in dirs:
            next_x = x + dx[i]
            next_y = y + dy[i]
            while True:
                if next_x >= M or next_x < 0 or next_y >= N or next_y < 0:
                    break
                if temp[next_y][next_x] == 6:
                    break
                temp[next_y][next_x] = 7
                next_x += dx[i]
                next_y += dy[i]
    res = min(res,check(temp))


def deep_copy():
    temp = [[0 for col in range(M)] for row in range(N)]
    for row in range(N):
        for col in range(M):
            temp[row][col] = graph[row][col]
    return temp


if __name__ == '__main__':
    res = float('inf')
    dx = (0,1,0,-1)
    dy = (-1,0,1,0)
    N, M = map(int, input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    tvs = list()
    init()
    dfs(0,[-1 for _ in range(len(tvs))])
    print(res)