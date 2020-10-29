# class Queue:
#     def __init__(self):
#         self.arr = []
#         self.front = 0
#         self.count = 0
#
#     def enqueue(self, data):
#         self.arr.append(data)
#         self.count += 1
#
#     def dequeue(self):
#         if self.count == 0:
#             return -1
#         element = self.arr[self.front]
#         self.front += 1
#         self.count -= 1
#         return element
#
#     def Front(self):
#         if self.count == 0:
#             return -1
#         return self.arr[self.front]
#
#     def size(self):
#         return self.count
#
#     def isEmpty(self):
#         return self.count == 0

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def enqueue(self, data):
#         node = Node(data)
#         if self.head == None and self.tail == None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node
#         self.count += 1
#
#     def dequeue(self):
#         if self.count == 0:
#             print("Queue is empty")
#             return
#         data = self.head.data
#         self.head = self.head.next
#         self.count -= 1
#
#     def front(self):
#         if self.count == 0:
#             print("Queue is empty")
#             return
#         return self.head.data
#
#     def size(self):
#         return self.count
#
#     def isEmpty(self):
#         return self.count == 0
class Queue:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
        self.count = 0

    def Enqueue(self, data):
        while len(self.arr1) != 0:
            self.arr2.append(self.arr1.pop())
        self.arr1.append(data)
        self.count += 1
        while len(self.arr2) != 0:
            self.arr1.append(self.arr2.pop())
        return

    def Dequeue(self):
        if self.QisEmpty():
            print("Queue is Empty")
            return
        return self.arr1.pop()
        self.count -= 1

    def QFront(self):
        if self.count == 0:
            return -1
        return self.arr1[-1]

    def Qsize(self):
        return self.count

    def QisEmpty(self):
        return self.count == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
while(q.isEmpty() is False):
    print(q.front())
    q.dequeue()
print(q.isEmpty())
print(q.dequeue())