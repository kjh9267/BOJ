def gcd(a, b):
    global depth
    depth += 1
    print(depth)
    if (b == 0): return a
    if (a == 0): return b
    return gcd(b, a % b)



if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    depth = 0
    # print(gcd(18,12))
    # print(gcd(3, 4))
    # print(gcd(12, 18))
    # print(12 % 18)

    print(gcd(100_000, 9999))