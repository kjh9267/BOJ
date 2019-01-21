#  반올림
#  https://www.acmicpc.net/problem/2033

input = __import__('sys').stdin.readline

if __name__ == '__main__':
    N = int(input())
    x = 1
    while N > x * 10:
        N += x * 5
        x *= 10
        N -= N % x

    print(N)