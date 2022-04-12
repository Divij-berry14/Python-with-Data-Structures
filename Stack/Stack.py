from collections import deque
from queue import LifoQueue

stack = LifoQueue(maxsize=3)
print(stack.qsize())
stack.put("a")
stack.put("b")
stack.put("c")
print("Full", stack.full())
print("Size", stack.qsize())
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ", stack.empty())


stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack:')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)