# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7
li2.append(5)
print(li2)
print(li1)
# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")



class A:
	def __init__(self, n):
			self.name = n
class B(A):
	def __init__(self, roll,name):
			self.roll = roll
			A.__init__(self,name)

object = B(23,"as")
print (object.name)
