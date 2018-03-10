import sys


def change():
    x = dx[signal[2]] + signal[0]
    y = dy[signal[2]] + signal[1]
    return x,y


def direction(a):
    if a is 0:
        print('U')
    elif a is 1:
        print('R')
    elif a is 2:
        print('D')
    else:
        print('L')


n, m = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
pr, pc = map(int,sys.stdin.readline().split())
dx = (0,1,0,-1)
dy = (-1,0,1,0)

time = [0,0,0,0]

for i in range(4):
    signal = [pc-1, pr-1, i]
    while True:
        x, y = change()
        signal[0] = x
        signal[1] = y
        time[i] += 1
        if not 0 <= x < m or not 0 <= y < n:
            break
        if graph[y][x] == 'C':
            break
        elif graph[y][x] == '/':
            if signal[2] is 0 or signal[2] is 2:
                signal[2] += 1
            elif signal[2] is 1 or signal[2] is 3:
                signal[2] -= 1
        elif graph[y][x] == "\\":
            if signal[2] is 0:
                signal[2] += 3
            elif signal[2] is 1:
                signal[2] += 1
            elif signal[2] is 2:
                signal[2] -= 1
            else:
                signal[2] -= 3
        if time[i] > 250000:
            direction(i)
            print('Voyager')
            exit()

direction(time.index(max(time)))
print(max(time))