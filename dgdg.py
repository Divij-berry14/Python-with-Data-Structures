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
class Person:
  def __init__(self, id):
    self.id = id

sam = Person(100)

sam.__dict__['age'] = 49

print(sam.age + len(sam.__dict__))

def my_func(num):
  data = [0]
  for i in range(1, num+1):
    data.append(data[i >> 1] + int(i & 1))
  return data


num = 6
print(my_func(num))

val1=28**0
val2=2.5
val3='123'
val4=int(val3)
print(val1+val2+val4)