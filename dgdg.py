# def min1(li):
#     l=len(li)
#     li.sort()
#     li1=[]
#     for i in range(l):
#         j=i+1
#         for j in range(l-1):
#             if(li[i]%2==0):
#                 temp=li[i]//2
#                 diff=abs(temp-li[j])
#                 li1.append(diff)
#     m=min(li1)
#     return m
#
#
# li=list(map(int, input.split()))
# out=min1(li)
# print(out)
# class Person:
#   def __init__(self, id):
#     self.id = id
#
# sam = Person(100)
#
# sam.__dict__['age'] = 49
#
# print(sam.age + len(sam.__dict__))
#
# def my_func(num):
#   data = [0]
#   for i in range(1, num+1):
#     data.append(data[i >> 1] + int(i & 1))
#   return data
#
#
# num = 6
# print(my_func(num))
#
# val1=28**0
# val2=2.5
# val3='123'
# val4=int(val3)
# print(val1+val2+val4)

# def prime(num):
#   res = []
#   temp = 2
#   for i in range(2, num+1):
#     if i%2 == 0:
#       continue
#     else:
#       res.append(i)
#
#   for i in res:
#     print(i, end=" ")
#
# prime(10)

# class Test:
#   def add(self, v1, v2):
#     ans = v1+v2
#     print(ans)
#
# obj = Test()
# obj.add(1, 2)

# def sum(v1,v2):
#   print(v1+v2)
#
# sum(1,2)
# print(v1,v2)


# Python program to show that we can create
# instance variables inside methods

# Class for Computer Science Student

# Python example to show the working of multiple
# inheritance

# Python program to
# demonstrate protected members


# Creating a base class
class Base:
  def __init__(self):
    # Protected member
    self.a = 2


# Creating a derived class
  class Base:
    def __init__(self):
      self.a = "GeeksforGeeks"
      self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
  def __init__(self):
    # Calling constructor of
    # Base class
    Base.__init__(self)
    print("Calling private member of base class: ")
    print(self.__c)


# Driver code
obj1 = Derived()
print(obj1.c)








