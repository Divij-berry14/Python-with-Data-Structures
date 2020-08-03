# class Student:
#     pass
# 
# s1=Student()
# s2=Student()
# s3=Student()
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(list))
# s1.name="Divij"
# s2.rollnumber=217055
# s3.name="Berry"
# s3.rollnumber=55
# print(s1.name)
# print(s3.name)
# print(s3.rollnumber)
# print(s3.__dict__)
# print(hasattr(s1,"name"))
# 
# #CHECKS IF THE PARTICUALR OBJECT HAS THE ATTRIBUTE OR NOT// RETURN TRUE OR FALSE
# #getattr(object,attribute,default(optional/if the attribute is not there in the object gives default value other than error))
# #delattr(object,attribute) deletes the attribute the object contains
# 
# 
# class Student:
#     def __init__(self,name,rollnumber):
#         self.name=name
#         self.rollnumber=rollnumber
#     
#     def print_student(self):
#         print("My name is",self.name,"and my roll number is",self.rollnumber)
# s1=Student("Divij",71055)
# s2=Student("Berry",55)
# s1.print_student()
# Student.print_student(s1)
# s2.print_student()
# print(s1.__dict__,s2.__dict__,end=' ')
# 
# 
# class Fraction:
#     def __init__(self,num=0,den=1):
#         if(den==0):
#             den=1
#         self.num=num
#         self.den=den
#     
#     def print_fraction(self):
#         if(self.num==0):
#             print(0)
#         elif(self.den==1):
#             print(self.num)
#         else:
#             print(self.num,'/',self.den)
#     
#     def simplify(self):
#         if(self.num==0):
#             self.den=1
#             return
#         current=min(self.num,self.den)
#         while(current>1):
#             if(self.num%current==0 and self.den%current==0):
#                 break
#             current-=1
#         self.num=self.num//current
#         self.den=self.den//current
#     
#     def add(self,otherFraction):
#         newNum=self.num * otherFraction.den + otherFraction.num*self.den
#         newDen=self.den * otherFraction.den
#         self.num=newNum
#         self.den=newDen
#         self.simplify()
#     
#     def multiply(self,otherFraction):
#         newNum=self.num * otherFraction.num
#         newDen=self.den * otherFraction.den
#         self.num=newNum
#         self.den=newDen
#         self.simplify()
#         
# F=Fraction(2,3)
# print(F.__dict__)
# F1=Fraction(2,0)
# print(F1.__dict__)
# F2=Fraction(4,3)
# F.print_fraction()
# F1.print_fraction()
# F2.simplify()
# F2.print_fraction()
# F.add(F2)
# F.print_fraction()
# F.multiply(F2)
# F.print_fraction()
# 
# 
# 
# class Complex_Number:
#     def __init__(self,R=0,I=0):
#         self.R=R
#         self.I=I
#     def print_Complex_Number(self):
#         if(self.R==0):
#             print('i',self.I)
#         elif(self.I==0):
#             print('i',self.R)
#         else:
#             print(self.R,'+','i',self.R)
#     def add(self,otherCNumber):
#         newR=self.R + otherCNumber.R
#         newI=self.I + otherCNumber.I
#         self.R=newR
#         self.I=newI
#     def multiply(self,otherCNumber):
#         newR=(self.R * otherCNumber.R) - (self.I * otherCNumber.I)
#         newI=(self.R * otherCNumber.I) + (otherCNumber.R * self.I)
#         self.R=newR
#         self.I=newI
#         
# 
#             
# C1=Complex_Number(4,5)
# C1.print_Complex_Number()
# C2=Complex_Number(6,7)
# C2.print_Complex_Number()
# C1.add(C2)
# C1.print_Complex_Number()
# C3=Complex_Number(4,5)
# C4=Complex_Number(6,7)
# C3.multiply(C4)
# C3.print_Complex_Number()
# name="Mohan"
# class Person():
#
#     # def __init__(self,name):
#     #     self.name=name
#     def printName(self,age):
#         global name
#         name="mo"
#         a="Divij"
#         # print(self.name)
#         print(name)
#         print(a)
#         print(age)
#     print(name)
#
# p=Person()
# p.printName(12)

# class emp:
#     def __init__(self):
#         self.name = 'xyz'
#         self.salary = 4000     #instance variables
#         self.a=0
#
#     def show(self):
#         a=0
#         print(self.name)
#         print(self.salary)
#
#
# e1 = emp()
# print("Dictionary form :", vars(e1))   # vars()– This function displays the attribute of an instance in the form of an dictionary.
# print(dir(e1))  # dir()– This function displays more attributes than vars function,as it is not limited to instance.
# # It displays the class attributes as well. It also displays the attributes of its ancestor classes.
#
# class sampleclass:
#     count = 0  # class attribute
#
#     def increase(self):
#         sampleclass.count += 1
#
#
# # Calling increase() on an object
# s1 = sampleclass()
# s1.increase()
# print(s1.count)
# print("var",vars(s1))
#
# # Calling increase on one more
# # object
# s2 = sampleclass()
# s2.increase()
# print(s2.count)
# print("dir",dir(s2))
#
# print(sampleclass.count)



# Python code to demonstrate how parent constructors
# are called.
# parent class
# class Person(object):
#
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
#     # child class
#
#
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
#
#     # creation of an object variable or an instance
#
#
# a = Employee('Rahul', 886012,123,"manager")
#
# # calling a function of the class Person using its instance
# a.display()


class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    def __init__(self, name,roll):
        self.roll = roll
        A.__init__(self,name)   #if this is not mentioned then error will be there
                                 #AttributeError: 'B' object has no attribute 'name'
object = B("divij",23)
print(object.name)


x=0
class Fruit:
    def __init__(self):
        global x
        x=x+1
        print("I am a fruit")
    def print(self):
        print("hi")

class Citrus(Fruit):
    def __init__(self):
        global x
        x+=2
        print("I am a citrus fruit",x)
        print(x)
        super().print()
        # Fruit.__init__(self)

lime=Citrus()


class C():
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


object1 = D()

# produces an error as d is private instance variable
print(object1.d)



# Python program to demonstrate
# super function
class Animals:

    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True

    def isMammal(self):
        if self.isMammal:
            print("It is a mammal.")

    def isDomestic(self):
        if self.mammals:
            print("It is a domestic animal.")


class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()


class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")

        # Dirver code


Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()
