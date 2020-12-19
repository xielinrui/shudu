import sys

able_number = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

default = [[0, 2, 1, 0, 6, 5, 4, 0, 0],
           [9, 7, 5, 3, 0, 0, 6, 2, 0],
           [0, 6, 4, 2, 0, 1, 3, 7, 5],
           [6, 0, 8, 5, 0, 2, 0, 4, 0],
           [5, 0, 0, 0, 3, 0, 0, 1, 0],
           [0, 1, 0, 0, 8, 0, 0, 0, 0],
           [0, 8, 6, 0, 0, 0, 7, 0, 0],
           [0, 9, 0, 0, 0, 3, 1, 0, 0],
           [0, 5, 0, 6, 7, 4, 8, 9, 0]]


def check_fu1(old1):
    for x in old1:
        if 0 in x:
            return True


def get_column_number(i: int, old1):
    ans = set()
    for x in old1[i]:
        if x != 0:
            ans.add(x.__str__())
    return ans


def get_row_number(j: int, old1):
    ans = set()
    for i in range(0, len(old1)):
        if old1[i][j] != 0:
            ans.add(old1[i][j].__str__())
    return ans


def get_zhengfangxing_number(i: int, j: int, old1):
    x = int(i / 3) * 3
    y = int(j / 3) * 3
    ans = set()
    for x_begin in range(x, x + 3):
        for y_begin in range(y, y + 3):
            if old1[x_begin][y_begin] != 0:
                ans.add(old1[x_begin][y_begin].__str__())
    return ans


def get_one_ans(i: int, j: int, old1):
    zhengfangxing = get_zhengfangxing_number(i, j, old1)
    column = get_column_number(i, old1)
    row = get_row_number(j, old1)
    ans = able_number - zhengfangxing
    ans = ans - column
    ans = ans - row
    # print(i,j,ans)
    return ans


def print_old(old1):
    n = len(old1)
    for i in range(0, n):
        m = len(old1[i])
        ans = ''
        for j in range(0, m):
            ans = ans + old1[i][j].__str__() + ','
        print(ans)


def get_result(old1):
    if not check_fu1(old1):
        print_old(old1)
        return True
    n = len(old1)
    flag = 0
    for i in range(0, n):
        m = len(old1[i])
        for j in range(0, m):
            if old1[i][j] == 0:
                ans = get_one_ans(i, j, old1)
                if len(ans) == 0:
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 1:
        # todo 说明出现了错误，需要回退
        return False
    for i in range(0, n):
        m = len(old1[i])
        for j in range(0, m):
            if old1[i][j] == 0:
                ans = get_one_ans(i, j,old1)
                for x in ans:
                    new = old1
                    new[i][j] = x
                    if get_result(new):
                        return True
                    new[i][j] = 0
                old1[i][j] = 0
                return False
    return False


if __name__ == '__main__':
    input_value = sys.argv[1]
    old = default
    i = 0
    j = 0
    for x in input_value:
        old[i][j] = int(x)
        if j == 8:
            i += 1
            j = 0
        else:
            j += 1
    ans1 = get_result(old)
    print(ans1)
