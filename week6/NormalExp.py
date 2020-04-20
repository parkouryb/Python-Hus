from week6.StringExp import StringExp


class NormalExp(StringExp):
    def __init__(self, exp):
        super().__init__(exp)

    def pre_infix(self):
        newExp = ""
        count = 0
        for c in self.exp:
            if c in "+*/()[]{}":

                if count != 0:
                    if count % 2 == 0:
                        newExp += "+"
                    else:
                        newExp += "-"
                    count = 0
                if c in "([{":
                    newExp += '('
                elif c in ")]}":
                    newExp += ')'
                else:
                    newExp += c
                continue
            if c in "0123456789":
                if count != 0:
                    if count % 2 == 0:
                        newExp += "+"
                    else:
                        newExp += "-"
                    count = 0
                newExp += c

                continue
            if c in ' ':
                newExp += " "
                continue
            if c in '-':
                count += 1
                continue
        return newExp

    def precedence(self, c):
        if c in "+-":
            return 1
        elif c in "*/":
            return 2
        elif c in "^":
            return 3
        return -1

    def infix_to_postfix(self):
        result = ""
        stack = []
        number = ""
        # check negative number
        operator_flag = False
        operand_flag = False
        negative_count = 0
        exp = self.pre_infix()
        for c in exp:
            if c in " ":
                continue
            if self.precedence(c) > 0:
                # if c is operator
                if number != "":
                    # pushing number to result
                    result += "(" + number + ")"
                number = ""
                while len(stack) is not 0 and self.precedence(stack[- 1]) >= self.precedence(c):
                    result += stack.pop()
                stack.append(c)
            else:
                if c in ")":
                    if number != "":
                        # pushing number to result
                        result += "(" + number + ")"
                    number = ""

                    # close bracket
                    x = stack.pop()
                    while x != "(":
                        result += x
                        x = stack.pop()

                else:
                    if c in "(":
                        # open bracket
                        number = ""
                        stack.append(c)
                    else:
                        # number
                        number += c
        if number != "":
            # pushing number to result
            result += "(" + number + ")"

        while len(stack) != 0:
            result += stack.pop()

        return result

    def compute(self):
        if not super(NormalExp, self).isValid():
            return None
        number = ""
        stack = []
        ope_stack = []
        exp = self.infix_to_postfix()
        count_operator = 0
        for c in exp:
            if c in ' ':
                continue
            if c in '([{':
                number = ""
            if c in "0123456789":
                number += c
            if c in ')]}':
                stack.append(number)
            if c in "+-*/":
                first_value = stack.pop()
                if len(stack) == 0:
                    stack.append(str(eval(str(0) + c + first_value)))
                    continue
                second_value = stack.pop()

                result = 0
                result = eval(second_value + c + first_value)
                stack.append(str(result))
        return stack.pop()


if __name__ == '__main__':
    ne = NormalExp("(1 + 2 + 31 / (4 * 5) + 5) + 0")
    # (1) - +(2) + -(3) * (4)(5) / +
    # (1)-+(2)+-(3)*(4)(5)/+
    # (1)-+(2)+-(3)*(4)(5)/+
    print(ne.pre_infix())
    print(ne.infix_to_postfix())
    print(ne.compute())