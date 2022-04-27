def check_redundant_brackets(string):
    s = []
    for char in string:
        if char is "(":



string_ = input()
ans = check_redundant_brackets(string_)
if ans is True:
    print("True")
else:
    print("False")