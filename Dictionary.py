a={1:2,3:4,"list":[1,23],"dict":{1:2}}
print(a[1])
print(a.get("list"))
print(a.get("li", 0)) # If the key is not present then it will return 0. Use of get will not show runtime error
print(a.keys())
print(a.values())
print(a.items()) # it will get key:value pairs

print("loop dic")
for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

print("list" in a) # to check if the key exist or not. It will return TRUE

a["t"]=(1,2,3,4)  # To add another key in the dictionary a
print(a)

b={3:5,'the':4,2 :100}
a.update(b)  # This function will update dictionary a on the basis of b dict
print(a) #{1: 2, 3: 5, 'list': [1, 23], 'dict': {1: 2}, 'tuple': (1, 2, 3, 4), 'the': 4, 2: 100}

print(a.pop('t'))  #Pop fucntion requires 1 arguement
del a[1]
print(a)

#Program to print words having frequency k
s= "This is a word string having many many word"
words=s.split()
d={}
for w in words:
    d[w]=d.get(w, 0)+1
print(d)
for w in d:
    if d[w] == 2:
        print(w)


