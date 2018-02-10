s = raw_input()
a = ''
for i in range(len(s)):
    if s[i] not in 'CAMBRIDGE':
        a += s[i]
print a