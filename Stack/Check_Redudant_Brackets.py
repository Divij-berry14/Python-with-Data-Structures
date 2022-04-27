def check_redundant_brackets(string):
    s = []
    flag_char = False
    for char in string:
        if char == "(" or flag_char is True and char != ")":
            s.append(char)
            flag_char = True

        elif char == ")":
            flag = False
            while not is_empty(s) and top(s) != "(":
                s.pop()
                flag = True

            if not flag:
                return True

            if not is_empty(s):
                s.pop()
    return False


def is_empty(stack):
    return len(stack) == 0


def top(stack):
    return stack[len(stack) - 1]


string_ = input()
print(check_redundant_brackets(string_))
