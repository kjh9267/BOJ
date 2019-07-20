if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    t = int(input())

    cnt = 0
    for _ in range(t):
        s = input().rstrip()

        res = True

        for i in range(len(s) - 1):
            if s[i] == 'C' and s[i + 1] == 'D':
                res = False

        if res:
            cnt += 1
    print(cnt)
