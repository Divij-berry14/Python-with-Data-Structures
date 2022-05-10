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