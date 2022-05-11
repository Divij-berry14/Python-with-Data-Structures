class QueueUsing2stacks:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []
    
    def enqueue(self, data):
        #O(n)
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        
        self.__s1.append(data)
        
        while len(self.__s2) != 0:
            self.__s1.append(self.__s2.pop())
        return
    
    def dequeue(self):
        #O(1)
        if len(self.__s1) == 0:
            return -1
        return self.__s1.pop()
    
    def q_front(self):
        if len(self.__s1) == 0:
            return -1
        return self.__s1[-1]
    
    def q_size(self):
        return len(self.__s1)
    
    def is_empty(self):
        return self.q_size() == 0
    
    
q = QueueUsing2stacks()
q.enqueue(34)
q.enqueue(45)
q.enqueue(23)
q.enqueue(12)
print("Front element of the queue is:", q.q_front())
print("If the elememt is empty of full", q.is_empty())
print("Size of the queue:", q.q_size())
print("Elements of the queue:")
while q.is_empty() is False:
    print(q.q_front())
    q.dequeue()
