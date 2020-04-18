import math

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0: return False
    return True

def plus_digit_in_number(n):
    sn = 0
    for digit in str(n):
        sn += int(digit)
    return sn

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def findLuckyNumber(filename):
    f = open(filename, "r", encoding="utf-8")
    # print(f.read())
    number = f.read().split()
    res = 0
    for num in number:
        if num.isnumeric():
            # print(num)
            if is_prime(int(num)):
                # print(num, plus_digit_in_number(int(num)))
                if plus_digit_in_number(int(num)) % 5 == 0:
                    res = int(num)
    return res

def get_ans(str1, str2):
    c = str2[::-1]

    return str1 == c

def findCouple(filename):
    f = open(filename, "r", encoding="utf-8")
    # print(f.read())
    ls = f.read().split()
    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):

            # print(ls[i], ls[j], "aaa" == "aaa")
            x = ls[j][::-1]
            y = ls[i][::-1]
            if ls[i] != y and ls[j] != x:
                if get_ans(ls[i], ls[j]):
                    # print("dcm")
                    if ls[i] > ls[j]: return ls[j], ls[i]
                    else: return ls[i], ls[j]
    return 'None', 'None'


def main():
    filename = "test.txt"
    print(findCouple(filename))

if __name__ == '__main__':
    main()