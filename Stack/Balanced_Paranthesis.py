def is_balanced(st):
    s = []
    for char in st:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if not s or s[-1] != '(':
                return False
            s.pop()
        elif char is '}':
            if not s or s[-1] != '{':
                return False
            s.pop()
        elif char is ']':
            if not s or s[-1] != '[':
                return False
            s.pop()
    if not s:
        return True
    return False


string = input()
ans = is_balanced(string)
if ans:
    print("true")
else:
    print("false")