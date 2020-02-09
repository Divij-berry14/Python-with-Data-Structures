class Student:
    pass

s1=Student()
s2=Student()
s3=Student()
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(list))
s1.name="Divij"
s2.rollnumber=217055
s3.name="Berry"
s3.rollnumber=55
print(s1.name)
print(s3.name)
print(s3.rollnumber)
print(s3.__dict__)
print(hasattr(s1,"name"))

#CHECKS IF THE PARTICUALR OBJECT HAS THE ATTRIBUTE OR NOT// RETURN TRUE OR FALSE
#getattr(object,attribute,default(optional/if the attribute is not there in the object gives default value other than error))
#delattr(object,attribute) deletes the attribute the object contains


class Student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    
    def print_student(self):
        print("My name is",self.name,"and my roll number is",self.rollnumber)
s1=Student("Divij",71055)
s2=Student("Berry",55)
s1.print_student()
Student.print_student(s1)
s2.print_student()
print(s1.__dict__,s2.__dict__,end=' ')


class Fraction:
    def __init__(self,num=0,den=1):
        if(den==0):
            den=1
        self.num=num
        self.den=den
    
    def print_fraction(self):
        if(self.num==0):
            print(0)
        elif(self.den==1):
            print(self.num)
        else:
            print(self.num,'/',self.den)
    
    def simplify(self):
        if(self.num==0):
            self.den=1
            return
        current=min(self.num,self.den)
        while(current>1):
            if(self.num%current==0 and self.den%current==0):
                break
            current-=1
        self.num=self.num//current
        self.den=self.den//current
    
    def add(self,otherFraction):
        newNum=self.num * otherFraction.den + otherFraction.num*self.den
        newDen=self.den * otherFraction.den
        self.num=newNum
        self.den=newDen
        self.simplify()
    
    def multiply(self,otherFraction):
        newNum=self.num * otherFraction.num
        newDen=self.den * otherFraction.den
        self.num=newNum
        self.den=newDen
        self.simplify()
        
F=Fraction(2,3)
print(F.__dict__)
F1=Fraction(2,0)
print(F1.__dict__)
F2=Fraction(4,3)
F.print_fraction()
F1.print_fraction()
F2.simplify()
F2.print_fraction()
F.add(F2)
F.print_fraction()
F.multiply(F2)
F.print_fraction()



class Complex_Number:
    def __init__(self,R=0,I=0):
        self.R=R
        self.I=I
    def print_Complex_Number(self):
        if(self.R==0):
            print('i',self.I)
        elif(self.I==0):
            print('i',self.R)
        else:
            print(self.R,'+','i',self.R)
    def add(self,otherCNumber):
        newR=self.R + otherCNumber.R
        newI=self.I + otherCNumber.I
        self.R=newR
        self.I=newI
    def multiply(self,otherCNumber):
        newR=(self.R * otherCNumber.R) - (self.I * otherCNumber.I)
        newI=(self.R * otherCNumber.I) + (otherCNumber.R * self.I)
        self.R=newR
        self.I=newI
        

            
C1=Complex_Number(4,5)
C1.print_Complex_Number()
C2=Complex_Number(6,7)
C2.print_Complex_Number()
C1.add(C2)
C1.print_Complex_Number()
C3=Complex_Number(4,5)
C4=Complex_Number(6,7)
C3.multiply(C4)
C3.print_Complex_Number()

