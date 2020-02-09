def is_balanced(string):
    s=[]
    for char in string:
        if char in '({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1]!='('):
                return False
            s.pop()
        elif char is '}':
            if (not s or s[-1]!='{'):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1]!='['):
                return False
            s.pop()
    if not s:
        return True
    return False

string=input()
ans=is_balanced(string)
print(ans)
