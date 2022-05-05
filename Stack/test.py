def sample(s)
    new_s = ""
    d = {}
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new_s = new_s + s[i]
    print(new_s + s[-1])
    temp = s.split("_")
    print(temp)
    for i in range(len(temp)):
        temp[i] = temp[i][0].upper() + temp[i][1:]
        # temp[i] = "".join(temp[i].split("")[0].upper())

    final_s = "".join(i[0].upper() + i[1:] for i in s.split("_"))
    print(final_s)
    # print("".join(temp))


# input = "hello_world_example"
# output = "HelloWorldExample
# input = 'aabbbaacccuusss'
# output = 'abacus'
sample("hello_world_example")