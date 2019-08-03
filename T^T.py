if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    a, b = map(int,input().split())
    c, d = map(int,input().split())

    m = b * d // __import__('math').gcd(b, d)

    x = m // b * a
    y = m // d * c

    u = x + y
    d = m

    g = __import__('math').gcd(u, d)
    print(u // g, d // g)