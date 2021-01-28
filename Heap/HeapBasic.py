import heapq

li = [5, 7, 8, 1, 4]
heapq.heapify(li)
print("The created heap is ", list(li))

heapq.heappush(li, 2)
print("After pushing an element", list(li))

heapq.heappop(li)
print("After poping an element", list(li))

li1 = [5, 7, 9, 4, 1]
li2 = [5, 7, 9, 4, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

print(li1)
print(li2)
# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 1))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 1))
print(li1)
print(li2)
