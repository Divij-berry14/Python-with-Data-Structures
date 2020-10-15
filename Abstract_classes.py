from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

o = A()
o.fun1()


from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

class B(A):

    def fun1(self):
        print("function 1 called")
o = B()
o.fun1()

from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

class B(A):

    def fun1(self):
        print("function 1 called")

    def fun2(self):
        print("function 2 called")
o = B()
o.fun1()



from abc import ABC,abstractmethod

class Automobile(ABC):
    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
        print("Automobile is created")
    
    @abstractmethod
    def start(self):
        print("Start Automobile is created")
    
    def stop(self):
        print("stop Automobile is created")
        
    def drive(self):
        pass
    

class Car(Automobile):
    
    def __init__(self):
        super().start()
        print("Car is created")
    def start(self):
        super().start()
        pass

    def stop(self):
        super().stop()
        pass
    def drive(self):
        pass

class Bus(Automobile):
    
    def __init__(self):
        print("Bus is created")
    def start(self):
        pass
    def stop(self):
        pass
    def drive(self):
        pass

c=Car()
c.start()
c.stop()
b = Bus()
b.start()
