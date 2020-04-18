import os

path = 'D:\\TrashPy\\Python-Hus\\docs'


def check_x(x, path, filename):
    f = open(path + "\\" + filename, 'r', encoding='utf-8')
    lines = f.read().split("\n")
    for line in lines:
        if x in line:
            return 'docs/' + filename, line + ' \n'
    return None, None


def searchInFiles(x, path):
    list_dir = os.listdir(path)
    data = {check_x(x, path, lldiv) for lldiv in list_dir if check_x(x, path, lldiv)[0] is not None}
    result = sorted(data, key= lambda x: x[0])
    return result


def zeroMove(fileName):
    f = open(fileName, 'r')
    data = f.read().split(' ')
    count_zeros = 0
    result = []
    for value in data:
        if value == '0':
            count_zeros += 1
        else:
            result.append(int(value))
    while count_zeros is not 0:
        result.append(0)
        count_zeros -= 1
    return result



# print(zeroMove('test.txt'))
print(searchInFiles("Anh", path))