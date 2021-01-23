# https://www.acmicpc.net/problem/2703


def match(x):
    if x == space:
        return space
    return cryptoquote[ord(x) - 65]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    space = ' '
    new_line = '\n'
    result = list()
    t = int(input())

    for _ in range(t):
        input_data = input().rstrip()
        cryptoquote = input().rstrip()
        output_data = ''.join(map(match, input_data))
        result.append(output_data)

    print(new_line.join(result))