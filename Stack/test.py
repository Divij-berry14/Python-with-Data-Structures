from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)



def reverseStack(inputStack, extraStack) :
    if len(inputStack) == 0:
        return;

    lastElement = inputStack.pop()
    print("dsd")

    reverseStack(inputStack, extraStack);

    while not isEmpty(inputStack):
        top = inputStack.pop()
        print("2w", top, inputStack)
        extraStack.append(top)

    inputStack.append(lastElement)
    print("1w",inputStack)
    while not isEmpty(extraStack):
        top = extraStack.pop()
        inputStack.append(top)
        print("3", inputStack)



'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0



#Taking input using fast I/o method
def takeInput() :
    size = int(stdin.readline().strip())
    inputStack = list()

    if size == 0:
        return inputStack


    values = list(map(int, stdin.readline().strip().split(" ")))
    inputStack = values

    return inputStack


#main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
    print(inputStack.pop(), end = " ")
