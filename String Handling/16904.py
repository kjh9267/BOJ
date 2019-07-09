s = input().rstrip()
pointer = 0
target = 'UCPC'
for idx, char in enumerate(s):
    if char == target[pointer]:
        pointer += 1
    if pointer == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')
