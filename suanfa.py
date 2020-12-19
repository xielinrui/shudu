import sys

old = [[0, 2, 1, 0, 6, 5, 4, 0, 0],
       [9, 7, 5, 3, 0, 0, 6, 2, 0],
       [0, 6, 4, 2, 0, 1, 3, 7, 5],
       [6, 0, 8, 5, 0, 2, 0, 4, 0],
       [5, 0, 0, 0, 3, 0, 0, 1, 0],
       [0, 1, 0, 0, 8, 0, 0, 0, 0],
       [0, 8, 6, 0, 0, 0, 7, 0, 0],
       [0, 9, 0, 0, 0, 3, 1, 0, 0],
       [0, 5, 0, 6, 7, 4, 8, 9, 0]]

able_number = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])


def check_fu1():
    for x in old:
        if 0 in x:
            return True


def get_column_number(i: int):
    ans = set()
    for x in old[i]:
        if x != 0:
            ans.add(x.__str__())
    return ans


def get_row_number(j: int):
    ans = set()
    for i in range(0, len(old)):
        if old[i][j] != 0:
            ans.add(old[i][j].__str__())
    return ans


def get_zhengfangxing_number(i: int, j: int):
    x = int(i / 3) * 3
    y = int(j / 3) * 3
    ans = set()
    for x_begin in range(x, x + 3):
        for y_begin in range(y, y + 3):
            if old[x_begin][y_begin] != 0:
                ans.add(old[x_begin][y_begin].__str__())
    return ans


def get_one_ans(i: int, j: int):
    zhengfangxing = get_zhengfangxing_number(i, j)
    column = get_column_number(i)
    row = get_row_number(j)
    ans = able_number - zhengfangxing
    ans = ans - column
    ans = ans - row
    return ans


def print_old():
    n = len(old)
    for i in range(0, n):
        m = len(old[i])
        ans = ''
        for j in range(0, m):
            ans = ans + old[i][j].__str__() + ','
        print(ans)


def get_result():
    cnt = 0
    while check_fu1():
        n = len(old)
        for i in range(0, n):
            m = len(old[i])
            for j in range(0, m):
                if old[i][j] == 0:
                    ans = get_one_ans(i, j)
                    if len(ans) == 1:
                        for x in ans:
                            old[i][j] = x
        print_old()
        cnt += 1
        print(cnt)


if __name__ == '__main__':
    input_value = sys.argv[1]
    print(input_value)
    i = 0
    j = 0
    for x in input_value:
        old[i][j] = int(x)
        if j == 8:
            i += 1
            j = 0
        else:
            j += 1
    print(old)
    get_result()
