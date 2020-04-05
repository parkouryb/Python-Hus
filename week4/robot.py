import math

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

def main():
    ptr = [-1, 3]
    # while (1):
    #     n = input()
    #     if not n:
    #         break
    #     s = n.split(" ")
    #     print(s)
    #     if (s[0] == "UP"):
    #         ptr[1] += int(s[1])
    #     else:
    #         if (s[0] == "DOWN"):
    #             ptr[1] -= int(s[1])
    #         else:
    #             if (s[0] == "LEFT"):
    #                 ptr[0] -= int(s[1])
    #             else:
    #                 if (s[0] == "RIGHT"): ptr[0] += int(s[1])

    print(round(3.4))


if __name__ == '__main__':
    main()
