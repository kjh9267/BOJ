if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    a, b, c = map(int,input().split())
    if c % 2 == 1:
        print(a^b)
    else:
        print(a^b^b)