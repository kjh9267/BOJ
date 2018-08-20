import sys

string = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]
key = False

for i in range(26):
    temp = ''
    for char in string:
        diff = ord(char) - i
        if diff < 97:
            temp += chr(123 - (97 - diff))
        else:
            temp += chr(diff)
    for word in words:
        if word in temp:
            key = True
            print(temp)
            exit()