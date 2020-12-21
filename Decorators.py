#CLOSURES

def outer():
    msg = "Hello World, People!"
    def inner():
        return msg
    return inner

a = outer()
print(a())
def outer_dec(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@outer_dec
def print_str():
    return "good morning"
print(print_str())


def div_decorator(func):
    def inner(x,y):
        if y==0:
            return "Give Proper Input"
        return func(x,y)
    return inner

@div_decorator
def div(x,y):
    return x/y

print(div(4,2))


def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()


# DECORATORS WITH PARAMETERS
def decorator_func(x, y):
    def Inner(func):
        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x + y))

            func(*args, **kwargs)

        return wrapper

    return Inner


# Not using decorator
@decorator_func(12, 15)
def my_fun(*args):
    for ele in args:
        print(ele)


# another way of using decorators
# decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
my_fun('Geeks', 'for', 'Geeks')


#Decoration on method
def check_name(method):
    def inner(name_ref):
        if name_ref.name == "Divij":
            print("Hey, my name is also same")
        else:
            method(name_ref)
    return inner

class Priting:
    def __init__(self, name):
        self.name = name

    @check_name
    def __call__(self, *args, **kwargs):
        print("Entered name is", self.name)


p = Priting("Divij")
print(p())  #calling object as a function


#CLASS BASED DECORATORS
class Check_divDeco:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i == 0:
                return "Given input is not valid"
            else:
                self.func(*args, **kwargs)

@Check_divDeco
def div(a, b):
    return a/b

@Check_divDeco
def div1(a, b, c):
    return a/b/c

print(div(10, 0))
print(div1(10, 0, 5))
