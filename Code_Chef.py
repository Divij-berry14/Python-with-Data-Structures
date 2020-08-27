# import dis
# print(dis.dis('for _ in [1,2,3]:pass'))

# li = [5, 7,  22, 97, 54, 62, 77, 23, 73, 61]
# res = filter(lambda x: (x%2 != 0), li)
# for i in res:
#     print(i)
# print(list(res))
print(list(map(lambda x:x%2==0,range(0,10))))
print(list(filter(lambda x:x*2,range(0,10))))