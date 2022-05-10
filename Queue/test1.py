class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLL:
    def __init__(self):
        self.count = 0
        self.front = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None and self.tail is None:
            self.front = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        element = self.front.data
        self.front = self.front.next
        self.count -= 1
        return element

    def queue_front(self):
        if self.front is None:
            print("Hey! Queue is Empty")
            return
        element = self.front.data
        return element

    def is_empty(self):
        return self.queue_size() == 0

    def queue_size(self):
        return self.count


q = QueueLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.queue_front())
while not q.is_empty():
    print(q.dequeue())
print(q.dequeue())

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
# class Queue:
#     def __init__(self):
#         self.arr1 = []
#         self.arr2 = []
#
#     def enqueue(self, data):
#         while len(self.arr1) != 0:
#             self.arr2.append(self.arr1.pop())
#         self.arr1.append(data)
#         while len(self.arr2) != 0:
#             self.arr1.append(self.arr2.pop())
#         return
#
#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#             return
#         return self.arr1.pop()
#
#     def front(self):
#         if len(self.arr1) == 0:
#             return -1
#         return self.arr1[-1]
#
#     def size(self):
#         return len(self.arr1)
#
#     def isEmpty(self):
#         return self.size() == 0
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# while(q.isEmpty() is False):
#     print(q.front())
#     q.dequeue()
# print(q.isEmpty())
# print(q.dequeue())

# import queue
# Q = queue.Queue(maxsize=3)
# print(Q.qsize())
# Q.put("a")
# Q.put("b")
# Q.put("c")
# Q.put("d")
# print(Q.full())
# print("Empty queue")
# print(Q.get())
# print(Q.get())
# print(Q.get())
# print(Q.get())
# print("Empty",Q.empty())
# Q.put(1)
# print(Q.empty())
# print(Q.full())

# from queue import Queue
#
# # Initializing a queue
# q = Queue(maxsize=3)
#
# # qsize() give the maxsize
# # of the Queue
# print(q.qsize())
#
# # Adding of element to queue
# q.put('a')
# q.put('b')
# q.put('c')
#
# # Return Boolean for Full
# # Queue
# print("\nFull: ", q.full())
#
# # Removing element from queue
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())
#
# # Return Boolean for Empty
# # Queue
# print("\nEmpty: ", q.empty())
#
# q.put(1)
# print("\nEmpty: ", q.empty())
# print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())
# import queue
#
# # From class queue, Queue is
# # created as an object Now L
# # is Queue of a maximum
# # capacity of 20
# L = queue.Queue(maxsize=20)
#
# # Data is inserted into Queue
# # using put() Data is inserted
# # at the end
# L.put(5)
# L.put(9)
# L.put(1)
# L.put(7)
#
# # get() takes data out from
# # the Queue from the head
# # of the Queue
# print(L.get())
# print(L.get())
# print(L.get())
# print(L.get())
