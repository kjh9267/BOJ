# https://www.acmicpc.net/problem/16391

if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    num = 0

    for _ in range(N):
        data = input().rstrip()
        if data == 'O':
            num = (num << 1) | 1
        else:
            num <<= 1

    print(num)