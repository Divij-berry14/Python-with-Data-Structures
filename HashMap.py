class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abs(hc)%(self.bucketSize))    #Compression function-->finding-> index=hashcode%bucketSize

    def insert(self, key, value):
        hc = hash(key)
        # print(hash)
        index = self.getBucketIndex(hc)
        # print(index)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1

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
                return head.value
            prev=head
            head=head.next
        return None

m=Map()
m.insert("Divij",1)
print(m.size())
m.insert("Berry",2)
print(m.size())
m.insert("Divij",3)
print(m.size())
m.insert("Divij",5)
print(m.size())
m.insert("Chirag",4)
print(m.size())
print("key Divij value is",m.getValue("Berry"))
m.removeKey("Berry")
print(m.getValue("Berry"))


