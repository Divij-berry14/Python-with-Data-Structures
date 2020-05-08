# a={1:2,3:4,"list":[1,23],"dict":{1:2}}
# print(a[1])
# print(a.get("list"))
# print(a.get("li", 0)) # If the key is not present then it will return 0. Use of get will not show runtime error
# print(a.keys())
# print(a.values())
# print(a.items()) # it will get key:value pairs
#
# print("loop dic")
# for i in a:
#     print(i,a[i])
#
# for i in a.values():
#     print(i)
#
# print("list" in a) # to check if the key exist or not. It will return TRUE
#
# a["t"]=(1,2,3,4)  # To add another key in the dictionary a
# print(a)
#
# b={3:5,'the': 4,2 :100}
# a.update(b)  # This function will update dictionary a on the basis of b dict
# print(a) #{1: 2, 3: 5, 'list': [1, 23], 'dict': {1: 2}, 'tuple': (1, 2, 3, 4), 'the': 4, 2: 100}
#
# print(a.pop('t'))  #Pop fucntion requires 1 arguement
# del a[1]
# print(a)
#
# #Program to print words having frequency k
# s= "This is a word string having many many word"
# words=s.split()
# d={}
# for w in words:
#     d[w]=d.get(w, 0)+1
# print(d)
# for w in d:
#     if d[w] == 2:
#         print(w)
#
# def checkMagazine(magazine, note):
#     dm={}
#     dn={}
#     for w in magazine:
#         dm[w]=dm.get(w,0)+1
#     for w in note:
#         dn[w]=dn.get(w,0)+1
#     for w in dn:
#         if w in dm and dn[w]<=dm[w]:
#             flag=1
#         else:
#             flag=0
#             break
#     print(dm)
#     print(dn)
#     if flag==1:
#         print("Yes")
#     else:
#         print("No")
#
# mn = input().split()
# m = int(mn[0])
# n = int(mn[1])
# magazine = input().rstrip().split()
# note = input().rstrip().split()
# checkMagazine(magazine, note)

# def numJewelsInStones(J,S):
#     d1 = {}
#     d2 = {}
#     for i in J:
#         d1[i] = d1.get(i, 0) + 1
#     for j in S:
#         d2[j] = d2.get(j, 0) + 1
#     print(d1,d2)
#     for w in d1:
#         if w in d2:
#             if d1[w] == d2[w]:
#                 return "true"
#             else:
#                 return "false"
#
# S="aa"
# J="aab"
# res=numJewelsInStones(S,J)
# print(res)
s="fihjjjjei"
j="hjibagacbhadfaefdjaeaebgi"
# d1={}
# d2={}
# for i in s:
#     d1[i] = d1.get(i, 0) + 1
# for i in j:
#     d2[i] = d2.get(i, 0) + 1
#
# # printing original dictionaries
# print("The original dictionary 1 : " + str(d1))
# print("The original dictionary 2 : " + str(d2))

# Using items() + <= operator
# Check if one dictionary is subset of other
# res = d1.items() <= d2.items()

# printing result
# print("Does dict2 lie in dict1 ? : " + str(res))
# if len(ransomNote)==0:
#     return True
# else:
#     return False
# for i in s:
#     if s.count(i)<=j.count(i):
#         flag=1
#     else:
#         flag=0
#         break
# if flag==0:
#     print("false")
# else:
#     print("true")
li=[int(x) for x in input().split()]
s=",".join(map(str,li))
s=s.split(",")
print(s)
d={}
for w in s:
    d[w]=d.get(w,0)+1
print(d)
max=0
for w in d:
    if max<d[w]:
        max=d[w]
        value=w
print(value)





