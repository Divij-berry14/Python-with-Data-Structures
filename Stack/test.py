# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, data):
#         self.data.append(data)
#
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#             return
#         return self.data.pop()
#     def isEmpty(self):
#         return self.size() == 0
#
#     def top(self):
#         if self.isEmpty():
#             print("I am Empty")
#             return
#         return self.data[len(self.data) -1]
#
#     def size(self):
#         return len(self.data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        value = self.head.data
        self.head = self.head.next
        self.count -= 1
        return value

    def top(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        data = self.head.data
        return data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
while s.isEmpty() is False:
    print(s.pop())
s.pop()
# print("end")
