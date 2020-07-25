# def qu(customers):
#     l = len(customers)
#     d = {}
#     li = []
#     for i in customers:
#         d[i] = d.get(i, 0) + 1
#     for j in d:
#         per = (d[j] / l) * 100
#         if per > 5:
#             li.append(j)
#     li.sort()
#     return li
#
# customers=["Omega","Alpha","Omega","Alpha","Omega","Alpha","Beta"]
# res=qu(customers)
# print(res)
def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
def mk2():
    print("Ordinary")
p = mk(mk2)
p()
print('{0:.4}'.format(2.0/3))
import re
expression="expression"
name = []
for j in re.finditer(expression, str):
    name.append(j.group(1))