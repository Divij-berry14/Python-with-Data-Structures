class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class Map:
    def __init__(self):
        self.bucketSize = 5
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketSize))    #Compression function-->finding-> index=hashcode%bucketSize

    def ReHash(self):
        temp=self.buckets
        self.buckets = [None for i in range(2*self.bucketSize)]
        self.count = 0
        self.bucketSize=2*self.bucketSize
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

    def LoadFactor(self):
        return self.count/self.bucketSize

    def insert(self, key, value):      #O(n)-->Time complexity
        hc = hash(key)   #O(L)--Time complexity
        # print(hash)
        index = self.getBucketIndex(hc)
        # print("index",index)
        head = self.buckets[index]
        while head is not None:   #O(n)--->t(n)=O(L)+O(N) which is equal to=O(n) because O(L)<<<O(N)
            if head.key == key:
                head.value = value
                return
            head = head.next
        head=self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        loadFactor = self.count/self.bucketSize
        if loadFactor >= 0.7:
            self.ReHash()

    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        else:
            return ("there is no value")

    def removeKey(self,key):
        hc=hash(key)
        index=self.getBucketIndex(hc)
        head=self.buckets[index]
        prev=None
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.buckets[index]=head.next
                else:
                    prev.next=head.next
                self.count-=1
                return head.value
            prev=head
            head=head.next
        return None

m=Map()
# m.insert("Divij",1)
# print(m.size())
# m.insert("Berry",2)
# print(m.size())
# m.insert("Divij",3)
# print(m.size())
# m.insert("Divij",5)
# print(m.size())
# m.insert("Chirag",4)
# print(m.size())
# print("key Divij value is",m.getValue("Berry"))
# m.removeKey("Berry")
# print(m.getValue("Berry"))
for i in range(10):
    m.insert("abc"+str(i),i+1)
    print(m.LoadFactor())

for i in range(10):
    print('abc'+str(i),m.getValue('abc'+str(i)))





