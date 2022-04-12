import queue
class Stack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.currSize = 0

    def push(self, data):
        size = self.q1.qsize()
        self.q1.put(data)
        for i in range(0, size):
            self.q1.put(self.q1.queue[0])
            self.q1.get()

    def pop(self):
        if self.q1.empty():
            print("No elements")
            return
        return self.q1.get()

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

    def Size(self):
        return self.q1.qsize()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("Curr size", s.Size())
print("top element", s.top())
print(s.pop())
print(s.pop())
print(s.Size())
print(s.top())