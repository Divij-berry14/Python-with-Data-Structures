class Queue_Using_Array:
    def __init__(self):
        self.__arr=[]
        self.__front=0
        self.__count=0
    
    def Enqueue(self,data):
        self.__arr.append(data)
        self.__count+=1
    
    def Dequeue(self):
        if self.__count==0:
            return -1
        element=self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return element
        
    def front(self):
        if self.__count==0:
            return -1
        return self.__arr[self.__front]
    
    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size()==0
    
q=Queue_Using_Array()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(4)
q.Enqueue(5)
while(q.isEmpty() is False):
    print(q.front())
    q.Dequeue()
print(q.isEmpty())
print(q.Dequeue())