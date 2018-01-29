from sys import stdin

k = int(stdin.readline())
n = int(stdin.readline())
player = [0 for _ in range(8)]
player[k-1] = 1
time = 0

for _ in range(n):
    bomb = player.index(1)
    t, z = stdin.readline().split()
    t = int(t)
    time += t
    if time >= 210:
        if time is 210:
            if z is 'T':
                print(bomb + 2)
                break
            else:
                print(bomb + 1)
                break
        else:
            print(bomb + 1)
            break
    if z is 'T':
        if bomb is 7:
            player[0] = 1
            player[7] = 0
        else:
            player[bomb] = 0
            player[bomb + 1] = 1