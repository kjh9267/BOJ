input = __import__('sys').stdin.readline

t = list(map(int,input().rstrip()))

if len(t) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    exit()
diff = t[0] - t[1]
def dfs(cur):

    if t[cur] - t[cur+1] != diff:
        return '흥칫뿡!! <(￣ ﹌ ￣)>'
    if cur == len(t) - 2:
        return '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'
    return dfs(cur + 1)


print(dfs(0))