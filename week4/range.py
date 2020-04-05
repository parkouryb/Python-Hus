def get_result(begin, end):
    s = [x for x in range(begin, end + 1) if x % 11 == 0 and x % 3 != 0]
    return '; '.join(str(x) for x in s)


def reverse_number(x):
    return int("".join(reversed(str(x))))


def get_dictionary(n):
    result = {}
    for i in range(0, n):
        result[i] = reverse_number(i * i)
    return result


def get_value_string(string):
    return string + "".join(reversed(string))


def input_strings():
    strings = input()
    strings = strings.split(" ")
    return strings


def main():
    # begin = 1010
    # end = 9090
    # print(get_result(begin, end))

    # print(get_dictionary(10))

    # strings = input_strings()
    # strings = ["abc", "aas", "x"]
    # dict = {}
    # for string in strings:
    #     dict[string] = get_value_string(string)
    # print(dict)

    # string = "0010"
    # num = int(string, 2)
    # print(num)

    # a = int(input("Input an integer : "))
    # n1 = int("%s" % a)
    # n2 = int("%s%s" % (a, a))
    # n3 = int("%s%s%s" % (a, a, a))
    # n4 = int("%s%s%s%s" % (a, a, a, a))
    # print (n1 + n2 + n3 + n4)

    a = []

    # create the table (name, age, job)
    a.append(["Tom", 19, 80])
    a.append(["John", 20, 90])
    a.append(["Jony", 17, 91])
    a.append(["Jony", 17, 93])
    a.append(["Json", 21, 85])

    # sort the table by age
    a.sort(key=lambda x: (x[0], x[2], x[1]))

    # print the table
    print(a)


if __name__ == '__main__':
    main()
