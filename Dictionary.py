a={1:2,3:4,"list":[1,23],"dict":{1:2}}
print(a.get("list"))
print(a.get("li",0)) # If the key is not present then it will return 0. Use of get will not show runtime error
print(a.keys())
print(a.values())
print(a.items()) # it will get key:value pairs

for i in a:
    print(i,a[i])