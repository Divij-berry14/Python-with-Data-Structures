class Stack:
    def __init__(self):
        self.__data = []
    
    def push(self, item):
        self.__data.append(item)
    
    def pop(self):
        if self.isEmpty():
            print("Hi! Stack is Empty!!")
            return
        
        return self.__data.pop()
    
    def top(self):
        if self.isEmpty():
            print("Hi! Stack is Empty!!")
            return
        
        return self.__data[len(self.__data)-1]
    
    def size(self):
        return len(self.__data)
    
    def isEmpty(self):
        return self.size() == 0
    
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Size of the stack is", s.size())
print("Top element of the Stack is:", s.top())
print("Pop elements are:")
while s.isEmpty() is False:
     print(s.pop())
print(s.top())