from sys import setrecursionlimit
setrecursionlimit(11000)


def reverse_stack(input_stack, empty_stack):
    while len(input_stack) == 0:
        return
    last_element = input_stack.pop()

    reverse_stack(input_stack, empty_stack)

    while not is_empty(input_stack):
        top = input_stack.pop()
        empty_stack.append(top)

    input_stack.append(last_element)

    while not is_empty(empty_stack):
        top = empty_stack.pop()
        input_stack.append(top)


def is_empty(stack):
    return len(stack) == 0


n = int(input())
s1 = [int(x) for x in input().split()]
s2 = []
reverse_stack(s1, s2)
while len(s1) != 0:
    print(s1.pop())