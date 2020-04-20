from unicodedata import numeric

from week6.StringExp import StringExp


class WellNetExp(StringExp):
    def __init__(self, exp):
        super().__init__(exp)

    def isWellNet(self):
        stack = []
        flag = True
        if not self.isValid():
            return False
        for c in self.exp:
            if c in " ":
                continue
            if c in "([{":
                stack.append([c, False, False, False])
            if c in "0123456789":

                if stack[-1][1] is False:
                    stack[-1][1] = True
                elif stack[-1][3] is False and stack[-1][2] is True:
                    stack[-1][3] = True
                else:
                    # print("debug: 1")
                    return False
            if c in "+-*/":
                if len(stack) == 0:
                    return False
                if stack[-1][2] is False:
                    stack[-1][2] = True
                else:
                    # print("debug 2")
                    return False

            if c in ")]}":
                if stack[-1][1] == stack[-1][2] and stack[-1][3] == stack[-1][2] and stack[-1][1] is True:
                    stack.pop()
                    if len(stack) is not 0:
                        if stack[-1][2] is True and stack[-1][1] is True:
                            # print("ok")
                            stack[-1][3] = True
                        stack[-1][1] = True
                else:
                    return False
        return True

    def precedence(self, c):
        if c in "+-":
            return 1
        elif c in "*/":
            return 2
        elif c in "^":
            return 3
        return -1

    def compute(self):
        if not self.isWellNet():
            return None
        operators = []
        operands = []
        for i in range(0, len(self.exp)):
            c = self.exp[i]
            if c.isnumeric():
                number = 0
                while c.isnumeric():
                    number *= 10
                    number += int(c)
                    i += 1
                    if i in range(0, len(self.exp)):
                        c = self.exp[i]
                    else:
                        break
                i -= 1

                operands.append(str(number))
            elif c in "([{":
                operators.append(c)
            elif c in ")]}":
                while not operators[-1] in "([{":
                    a = operands.pop()
                    b = operands.pop()
                    operator = operators.pop()
                    operands.append(str(eval(b + operator + a)))
                operators.pop()
            elif c in "+-*/":
                while len(operators) is not 0 and self.precedence(c) <= self.precedence(operators[-1]):
                    a = operands.pop()
                    b = operands.pop()
                    operator = operators.pop()
                    operands.append(str(eval(b + operator + a)))

                operators.append(c)
        while len(operators) != 0:
            a = operands.pop()
            b = operands.pop()
            operator = operators.pop()
            operands.append(str(eval(b + operator + a)))

        return int(operands.pop())


if __name__ == '__main__':
    wne = WellNetExp("(((1+2)+3)+45)")
    print(wne.compute())