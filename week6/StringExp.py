class StringExp:
    def __init__(self, exp):
        self.exp = exp

    def isValid(self):
        stack = []
        for c in self.exp:
            if c not in "(){}[]":
                continue
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c in ")":
                    if stack.pop() not in "(":
                        return False
                elif c in "]":
                    if stack.pop() not in "[":
                        return False
                elif c in "}":
                    if stack.pop() not in "{":
                        return False
            # print(stack)

        return len(stack) == 0


if __name__ == '__main__':
    se = StringExp("{{{")
    print(abs.__doc__)