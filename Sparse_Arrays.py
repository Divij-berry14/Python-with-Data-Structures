str_input=int(input())
li_string=[]
for i in range(str_input):
    current=input()
    li_string.append(current)

query_input=int(input())
li_query=[]
for j in range(query_input):
    curr=input()
    li_query.append(curr)

output_array=[]    
for m in li_query:
    count=0
    if m in li_string:
        c=li_string.count(m)
        output_array.append(c)
    else:
        output_array.append(0)
for ele in output_array:
    print(ele)

    