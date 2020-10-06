class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack_using_LL():
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
    
    def Enqueue(self,data):
        newNode=Node(data)
        if self.__head==None and self.__tail==None:
            self.__head=newNode
            self.__tail=newNode
        else:
            self.__tail.next=newNode
            self.__tail=newNode
        self.__count+=1
        
    def Dequeue(self):
        if self.__head is None:
            print("Hey! Queue is Empty")
            return
        element=self.__head.data
        self.__head=self.__head.next
        self.__count=self.__count-1
        return element
    
    def Queue_Front(self):
        if self.__head is None:
            print("Hey! Queue is Empty")
            return
        element=self.__head.data
        return element
    
    def isEmpty(self):
        return self.Qsize()==0
    
    def Qsize(self):
        return self.__count   #return Boolean, True/False
    
q=Stack_using_LL()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
q.Enqueue(6)
while q.isEmpty() is False:
    print(q.Dequeue())
print(q.Queue_Front())