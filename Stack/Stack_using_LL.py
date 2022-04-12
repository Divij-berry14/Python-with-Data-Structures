class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__count = self.__count+1
    
    def pop(self):
        if self.is_empty() is True:
            print("Hi! Stack is empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count-1
        return data
    
    def top(self):
        if self.is_empty() is True:
            print("Hi! Stack is empty")
            return
        data = self.__head.data
        return data
    
    def size(self):
        return self.__count
    
    def is_empty(self):
        return self.size() == 0
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Top element of the stack is", s.top())
print("Size of the stack is", s.size())
print("Elements after popping is:")
while s.is_empty() is False:
    print(s.pop())