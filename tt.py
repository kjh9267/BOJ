
if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    a, b, c = map(int,input().split(':'))
    x, y, z = map(int,input().split(':'))
    x = x + 23 - a
    y = y + 59 - b
    z = z + 60 - c
    y += z // 60
    z %= 60
    x += y // 60
    y %= 60
    x %= 24
    print("{:02d}:{:02d}:{:02d}".format(x,y,z))