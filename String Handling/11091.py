#  https://www.acmicpc.net/problem/11091

input = __import__('sys').stdin.readline

N = int(input())

for _ in range(N):
    chars = [0 for _ in range(26)]
    line = input().rstrip()

    for char in line:
        if 97 <= ord(char) < 123:
            chars[ord(char) - 97] += 1
        elif 65 <= ord(char) < 91:
            chars[ord(char) - 65] += 1

    missing = "".join(chr(index + 97) for index, cnt in enumerate(chars) if cnt == 0)

    if 0 in chars:
        print('missing {}'.format(missing))
    else:
        print('pangram')