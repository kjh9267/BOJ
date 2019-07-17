if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    mapping = {' ' : '%20',
               '!' : '%21',
               '$' : '%24',
               '%' : '%25',
               '(' : '%28',
               ')' : '%29',
               '*' : '%2a'
               }

    while True:
        line = input().rstrip()
        res = list()
        if line == '#':
            continue
        for i in line:
            if i in mapping:
                res.append(mapping[i])
            else:
                res.append(i)
        print(''.join(res))