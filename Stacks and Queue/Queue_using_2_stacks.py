class Queue_using_2_stacks():
    def __init__(self):
        self.__s1=[]
        self.__s2=[]
    
    def Enqueue(self,data):
        #O(n)
        while (len(self.__s1)!=0):
            self.__s2.append(self.__s1.pop())
        
        self.__s1.append(data)
        
        while(len(self.__s2)!=0):
            self.__s1.append(self.__s2.pop())
        return
    
    def Dequeue(self):
        #O(1)
        if(len(self.__s1)==0):
            return -1
        return self.__s1.pop()
    
    def Qfront(self):
        if len(self.__s1)==0:
            return -1
        return self.__s1[-1]
    
    def Qsize(self):
        return len(self.__s1)
    
    def isEmpty(self):
        return self.Qsize()==0
    
    
q=Queue_using_2_stacks()
q.Enqueue(34)
q.Enqueue(45)
q.Enqueue(23)
q.Enqueue(12)
print("Front element of the queue is:",q.Qfront())
print("If the elememt is empty of full",q.isEmpty())
print("Size of the queue:",q.Qsize())
print("Elements of the queue:")
while(q.isEmpty() is False):
    print(q.Qfront())
    q.Dequeue()
