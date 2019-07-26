
if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    while True:
        line = input().rstrip()
        if not line:
            break
        a, b = map(int,line.split())
        print('{:.2f}'.format(round(a / b, 2)))