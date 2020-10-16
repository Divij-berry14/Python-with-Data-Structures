class Queue:
    def __init__(self):
        self.arr = []
        self.front = 0
        self.count = 0

    def enqueue(self, data):
        self.arr.append(data)
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            return -1
        element = self.arr[self.front]
        self.front += 1
        self.count -= 1
        return element

    def Front(self):
        if self.count == 0:
            return -1
        return self.arr[self.front]

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
while(q.isEmpty() is False):
    print(q.Front())
    q.dequeue()
print(q.isEmpty())
print(q.dequeue())