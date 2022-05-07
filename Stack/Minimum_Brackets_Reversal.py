"""
For a given expression in the form of a string, find the minimum number of brackets that can be reversed
in order to make the expression balanced. The expression will only contain curly brackets.
If the expression can't be balanced, return -1.

Expression: {{{{
If we reverse the second and the fourth opening brackets, the whole expression will get balanced.
Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

Expression: {{{
In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence
 will not be able to make the expression balanced and the output will be -1.
"""


def min_bracket_reversal(s):
    if len(s) == 0:
        return 0
    if len(s) % 2 != 0:
        return -1
    li = []
    for i in s:
        if i == "{":
            li.append(i)
        else:
            if not is_empty(li) > 0 and top(li) == "{":
                li.pop()
            else:
                li.append(i)
    temp = len(li)
    if temp % 2 == 0:
        return temp // 2
    else:
        return -1


def is_empty(stack):
    return len(stack) == 0


def top(stack):
    return stack[len(stack) - 1]


string = input()
ans = min_bracket_reversal(string)
print(ans)

# {{{{}}