def input_bank():
    keys = []
    while (1):
        n = input()
        if not n:
            break
        s = n.split(" ")
        keys += [s[0], (int)(s[1])]
    # print(names)
    return keys

def main():
    keys = input_bank()
    amount = 0
    for k in keys:
        if (k[0] == "D"):
            amount += k[1]
        else: amount -= k[1]
    print(amount)

if __name__ == '__main__':
    main()