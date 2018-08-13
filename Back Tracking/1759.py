import sys


class Word:
    def __init__(self):
        self.word = ''


def dfs(cur):
    if cur == C:
        return

    if len(w.word + chars[cur]) == L:
        x = 0
        y = 0
        for i in w.word + chars[cur]:
            if ord(i) == 97 or ord(i) == 101 or ord(i) == 105 or ord(i) == 111 or ord(i) == 117:
                x += 1
            else:
                y += 1
        if x > 0 and y > 1:
            res.append(w.word + chars[cur])

    w.word += chars[cur]
    dfs(cur + 1)
    w.word = w.word[:-1]
    dfs(cur + 1)


L, C = map(int,sys.stdin.readline().split())
chars = sorted(list(sys.stdin.readline().split()))
res = []
w = Word()

dfs(0)

for i in res:
    print(i)
