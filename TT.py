if __name__ =='__main__':
    input = __import__('sys').stdin.readline

    data = [3, 5, 7, 9, 8, 0, 1, 4, 2, 6]

    print(data)

    # bubble
    # for i in range(10):
    #     for j in range(10 - i - 1):
    #         if data[j] > data[j + 1]:
    #             data[j + 1], data[j] = data[j], data[j + 1]

    # selection
    # for i in range(9):
    #     num = data[i]
    #     target = i
    #     for j in range(i, 10):
    #         if data[j] < num:
    #             num = data[j]
    #             target = j
    #     data[i], data[target] = data[target], data[i]



    print(data)