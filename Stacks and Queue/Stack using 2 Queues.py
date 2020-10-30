import queue
class Stack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.size = 0

    def push(self, data):
        self.size += 1
        self.q2.put(data)
        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):
        if self.q1.empty():
            return
        return self.q1.get()
        self.size -= 1

    def top(self):
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]

    def Size(self):
        return self.size

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print("Current Size", s.Size())
print(s.top())
print(s.pop())
print(s.top())
print(s.pop())
print(s.top())
print("Now curr size", s.Size())