if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    N , M = map(int,input().split())

    C = int(input())
    C*=2
    a = N + M

    if a >= C:
        print(a - C)
    else:
        print(a)