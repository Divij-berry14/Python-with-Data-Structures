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