from functools import reduce


def check_input(message):
    print(message)
    while True:
        page_number = input()
        if page_number.isnumeric() and int(int(page_number) % 16) == 0 and int(page_number) <= 1280:
            return int(page_number)
        print("Input is invalid, input should integer that not nore that 1280 and divisible by 16:  ")


def book_spliter(flag):
    def wrap(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if flag:
                if type(res) is list:
                    temp = []
                    for y in res:
                        res_list = []
                        for j in range(0, len(y), 4):
                            res_list.extend([[y[j], y[j + 1], y[j + 2], y[j + 3]]])
                        temp.append(res_list)
                    return temp
                else:
                    temp = []
                    for x in res:
                        for y in x:
                            res_list = []
                            for j in range(0, len(y), 4):
                                res_list.extend([[y[j], y[j + 1], y[j + 2], y[j + 3]]])
                            temp.append(res_list)
                    return temp
            else:
                if type(res) is list:
                    return res
                else:
                    temp = []
                    for x in res:
                        temp.extend(x)
                    return temp

        return wrapper

    return wrap


@book_spliter(False)
def create_book_blocks(page_number):
    book = list()
    for i in range(int(page_number / 16)):
        temp = i * 16
        temp_list = list()
        for j in range(0, 8, 2):
            temp_list.extend([temp + 16 - j, temp + j + 1, j + temp + 2, temp + 15 - j])
        book.append(temp_list)
    yield book  # you can change it to 'return'


page_number = check_input("Input number of pages: ")
print(create_book_blocks(page_number))
