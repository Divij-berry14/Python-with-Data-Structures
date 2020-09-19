class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'

    @email.setter
    def email(self, mail):
        names = mail.split("@")[0]
        self.first = names.split(".")[0]
        self.last = names.split(".")[1]

    @property
    def fullName(self):  #getter method
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name): #setter method
        first, last = name.split(" ")
        self.first = first
        self.last = last

emp1 = Employee('divij', 'berry')
emp1.first = "davij"
emp1.last = "berr"
emp1.email = "div.berry1999@gmailcom"
# emp1.fullName = "jimmy salvatore"
print(emp1.first)
print(emp1.last)
# print(emp1.fullName)
print(emp1.email)