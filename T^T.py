# https://www.acmicpc.net/problem/11659


if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    T = int(input())
    data = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

    maxi = 0
    res = 0
    for i in range(9):
        a = max(map(int,input().split()))
        if maxi < a:
            maxi = a
            res = i
    print(data[res])