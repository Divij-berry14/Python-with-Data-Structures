class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        if self.first == None and self.last == None:
            return "Email is not set. Please set it using setter"
        return self.first + '.' + self.last + '@email.com'

    @email.setter
    def email(self, mail):
        names = mail.split("@")[0]
        self.first = names.split(".")[0]
        self.last = names.split(".")[1]

    @email.deleter
    def email(self):
        self.first = None
        self.last = None

    @property
    def fullName(self):  #getter method
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name): #setter method
        first, last = name.split(" ")
        self.first = first
        self.last = last

emp1 = Employee('divij', 'berry')
print("before Mail-", emp1.email)
emp1.first = "davij"
emp1.last = "berr"
print("after Mail-", emp1.email)
print("after Full Name-", emp1.fullName)
emp1.email = "div1.berry999@gmailcom"
# emp1.fullName = "jimmy salvatore"
print("new-", emp1.first)
print("new-", emp1.last)
# print(emp1.fullName)
print("new-", emp1.email)
print("new-", emp1.fullName)
del emp1.email
print("delete email-", emp1.email)