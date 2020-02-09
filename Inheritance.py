#class Vehicle:
#    def __init__(self,color,maxSpeed):
#        self.color=color
#        self.__maxSpeed=maxSpeed
#        
#    def getMaxSpeed(self):
#        return self.__maxSpeed
#
#    def setMaxSpeed(self,maxSpeed):
#        self.__maxSpeed=maxSpeed
#
#class Car(Vehicle):
#    def __init__(self,color,maxSpeed,numGears,isConvertible):
#        super().__init__(color,maxSpeed)
#        self.numGears=numGears
#        self.isConvertible=isConvertible
#        
#    def printCar(self):
#        print("Color:",self.color)
#        print("Max Speed:",self.getMaxSpeed())
#        print("Num of Gears:",self.numGears)
#        print("is Convertible:",self.isConvertible)
#        
#c=Car("red",15,3,False)
#c.printCar()

#class Vehicle:
#
#	def __init__(self,color,maxSpeed):
#		self.color = color
#		self.__maxSpeed = maxSpeed
#
#	def getMaxSpeed(self):
#		return self.__maxSpeed
#
#	def setMaxSpeed(self,maxSpeed):
#		self.__maxSpeed = maxSpeed
#
#	def print(self):
#		print("Color :" ,self.color)
#		print("MaxSpeed :",self.__maxSpeed)
#
#class Car(Vehicle):
#
#	def __init__(self,color,maxSpeed,numGears,isConvertible):
#
#		super().__init__(color,maxSpeed)
#		self.numGears = numGears
#		self.isConvertible = isConvertible
#
#	def printCar(self):
#		self.print()
#		print("NumGears :",self.numGears)
#		print("IsConvertible :", self.isConvertible)
#
#
#c = Car("red",15,3,False)
#c.printCar()
## updating car speed even it is a private variable
#c.setMaxSpeed(50)
#c.printCar()

#class Vehicle:
#
#	def __init__(self,color,maxSpeed):
#		self.color = color
#		self.__maxSpeed = maxSpeed
#
#	def getMaxSpeed(self):
#		return self.__maxSpeed
#
#	def setMaxSpeed(self,maxSpeed):
#		self.__maxSpeed = maxSpeed
#
#	def print(self):
#		print("Color :" ,self.color)
#		print("MaxSpeed :",self.__maxSpeed)
#
#class Car(Vehicle):
#
#	def __init__(self,color,maxSpeed,numGears,isConvertible):
#
#		super().__init__(color,maxSpeed)
#		self.numGears = numGears
#		self.isConvertible = isConvertible
#
#	def print(self):
#		super().print() # Call the Base class
#       #self.print()   # Call the derived class again and again and give error MAX RECURSION DEPTH
#		print("NumGears :",self.numGears)
#		print("IsConvertible :", self.isConvertible)
#
#
#c = Car("red",15,3,False)
#c.print()


# METHOD OVERRIDING 
#class Vehicle:
#    def __init__(self,color):
#        self.color = color
#    def print(self):
#        print(c.color,end=" ")
#
#                                                       
#class Car(Vehicle):
#    def __init__(self,color,numGears):
#        super().__init__(color)
#        self.numGears = numGears
#    def print(self):                         # TWO PRINT FUNCTION
#       print(c.color,end=" ")
#       print(c.numGears)
#
#
#c = Car("black",5)
#c.print()

#PROTECTED CLASS/MEMBERS

#class Vehicle:
#
#	def __init__(self,color,maxSpeed):
#		self.color = color
#		self._maxSpeed = maxSpeed
#
#	@classmethod
#	def getMaxSpeed(cls):
#		return 15
#
#	def setMaxSpeed(self,maxSpeed):
#		self._maxSpeed = maxSpeed
#
#	def print(self):
#		print("Color :" ,self.color)
#		print("MaxSpeed :",self._maxSpeed)
#
#class Car(Vehicle):
#
#	def __init__(self,color,maxSpeed,numGears,isConvertible):
#
#		super().__init__(color,maxSpeed)
#		self.numGears = numGears
#		self.isConvertible = isConvertible
#
#	def print(self):
#		# super().print()
#		print("Color :" ,self.color)
#		print("MaxSpeed :",self._maxSpeed)
#		print("NumGears :",self.numGears)
#		print("IsConvertible :", self.isConvertible)
#
#
## c = Car("red",15,3,False)
## c.print()
##print()
#v = Vehicle("red",18)
#v.print()
#print()
#v._maxSpeed = 19
#get = v.getMaxSpeed()
#print(get)
#
#
# OBJECT CLASS
#class Circle(object):
#
#	def __init__(self,radius):
#		self.__radius = radius
# 
#	def __str__(self):   # IF THIS IS PRESENT IT WILL RETURN THE STATEMENT
#		return "This is a Circle class which takes radius as an argument."
#
#c = Circle(3)
#print(c)   #OUTPUT- <__main__.Circle object at 0x000001A1E93348D0>


#MULTIPLE INHERITANCE
#class Mother:
#
#	def __init__(self):
#		self.name = "Manju"
#		super().__init__()
#
#	def print(self):
#
#		print("Print Of Mother called")
#
#class Father:
#
#	def __init__(self):
#		self.name = "Ajay"
#		#super().__init__()
#	def print(self):
#
#		print("Print Of Father called",self.name)
#
#class Child(Mother,Father):
#    def __init__(self,name):
#        self.name=name
#        super().__init__()
#    
#    def print(self):
#        print("Name of child is", self.name)
#
#c = Child("Rohan")
#c.print()
#print(Child.mro())



import math
class Point:

	def __init__(self,x,y):
		self.__x = x
		self.__y = y


	def __str__(self):

		return "This point is at (" + str(self.__x) + "," + str(self.__y) + ")"

#	def __add__(self,point_object):
#		return Point(self.__x + point_object.__x,self.__y + point_object.__y)

	def __lt__(self,point_object): # LT=LESS THAN
		return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_object.__x**2 + point_object.__y**2)


p1 = Point(1,2)
print(p1)
p2 = Point(3,4)
print(p2)
#p3 = p1 + p2
#print(p3)
print(p2<p1)