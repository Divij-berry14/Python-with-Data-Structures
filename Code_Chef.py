# def reverse_decorator(function):
#     print("before everything 0")
#     def reverse_wrapper():
#         make_reverse = "".join(reversed(function()))
#         return make_reverse
#
#     return reverse_wrapper
#
#
# def uppercase_decorator(function):
#     print("before 1")
#     def uppercase_wrapper():
#         var_uppercase = function().upper()
#         return var_uppercase
#
#     return uppercase_wrapper
#
#
# @uppercase_decorator
# @reverse_decorator
# def say_hi():
#     return 'hi george'
#
#
# def main():
#     print(say_hi())
#
#
#
# print("shoudl print me first")
# main()
def dec(func):
    print("1")
    def inner(*args,**kwargs):
        print("2")
        m=func(10,20)
        return m
    return inner
@dec
def sum(a,b):
    return "i"

print("i shoudl be first")
print(sum(10,20))